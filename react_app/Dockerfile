# Use an official Node.js runtime as a parent image
FROM node:16-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./

# Install dependencies
# Include your custom libraries in the npm install command
RUN npm install --frozen-lockfile && \
    npm install axios @mui/material @emotion/react @emotion/styled @mui/x-data-grid @mui/icons-material react-router-dom@6.22.1 react-pro-sidebar formik yup @nivo/core @nivo/pie @nivo/line @nivo/bar @nivo/geo @babel/plugin-proposal-private-property-in-object @nivo/heatmap

WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json yarn.lock* ./

# Install dependencies
RUN npm install

# Bundle app source
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Define the command to run the app using npm start
CMD ["npm", "start"]
