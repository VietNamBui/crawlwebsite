# Build stage
FROM node:16-alpine AS build

WORKDIR /app

# Copy package files first for better caching
COPY package*.json ./

# Install dependencies using npm install instead of npm ci
RUN npm install --production

# Copy only necessary files
COPY public/ ./public/
COPY src/ ./src/

# Build app
RUN npm run build

# Production stage
FROM nginx:alpine

# Copy only build files
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]