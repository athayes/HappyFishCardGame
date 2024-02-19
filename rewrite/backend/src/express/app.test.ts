// Define your dependencies
const express = jest.fn(() => ({
    use: jest.fn(),
    listen: jest.fn(),
  }));
  
  // @ts-ignore
  express.json = jest.fn();
  
  const initializeDatabase = jest.fn();
  const setupRoutes = jest.fn();
  
  // Mock the modules
  jest.mock('express', () => express);
  jest.mock("../database/initialize", () => { return { initializeDatabase }});
  jest.mock("./routes", () => { return { setupRoutes }});
  
  // Import the function to test
  import { createApp } from "./app";
  
  describe("createApp", () => {
      let app;
  
      beforeEach(async () => {
          app = await createApp();
      });
  
      afterEach(() => {
          jest.clearAllMocks();
      });
  
      it("should create an express application", () => {
          expect(express).toHaveBeenCalled();
      });
  
      it("should use the JSON body parser", () => {
        // @ts-ignore
          expect(express.json).toHaveBeenCalled();
      });
  
      it("should setup routes", () => {
          expect(setupRoutes).toHaveBeenCalled();
      });
  
      it("should initialize the database", () => {
          expect(initializeDatabase).toHaveBeenCalled();
      });
  });