# Use the official Node.js image as a base image
FROM node:20.11.0

# Set the working directory in the container
WORKDIR /app/react_app

# Copy package.json and package-lock.json to the container
COPY react_app/package*.json ./

# Install dependencies
RUN npm install

# Copy the entire app to the container
COPY react_app .

# Build the app
RUN npm run build

# Expose the port your app will run on (assumed to be 3000 based on common setup)
EXPOSE 3000

# Command to run the application
CMD ["npm", "start"]

