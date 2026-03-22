ARG NODE_BASE=node:20-bullseye-slim
ARG NGINX_BASE=nginx:1.27-alpine

# 使用构建机架构构建前端，避免 QEMU 在 arm64 下执行 npm 导致非法指令
FROM --platform=$BUILDPLATFORM ${NODE_BASE} AS build
WORKDIR /app
COPY frontend/package*.json ./
ENV CI=1
RUN npm ci --no-audit --no-fund
COPY frontend .
RUN npm run build

FROM ${NGINX_BASE}
WORKDIR /usr/share/nginx/html
COPY --from=build /app/dist .
# 提供简易 Nginx 配置，转发 /api 到后端
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 5173 80
CMD ["nginx", "-g", "daemon off;"]
