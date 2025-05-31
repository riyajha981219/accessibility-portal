# Use an official Node image
FROM node:20

# Set working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose port (Vite uses 5173 by default)
EXPOSE 5173

# Start dev server
CMD ["npm", "run", "dev"]