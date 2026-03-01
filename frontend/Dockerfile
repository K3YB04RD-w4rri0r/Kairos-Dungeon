FROM node:20-slim AS build

WORKDIR /app

# Use Corepack (bundled with Node 20+) to install pnpm at a pinned version
RUN corepack enable && corepack prepare pnpm@9.15.0 --activate

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .
RUN pnpm build
# Note: The build succeeds with zero game assets. All 126 creature sprite sheets
# are pre-baked. If any PNG is missing at runtime, the fallback sprite pattern
# (S2.3.8) recovers via flesh base sprite + PixiJS tint/scale. No build-time
# asset validation is needed.

FROM nginx:1.27-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Run as non-root user in production (SEC-06)
RUN adduser -D -g "" appuser && \
    chown -R appuser:appuser /usr/share/nginx/html /var/cache/nginx /var/log/nginx /etc/nginx/conf.d /run
USER appuser

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget --spider -q http://localhost:8080 || exit 1
