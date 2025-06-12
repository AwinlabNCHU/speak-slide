import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.PROD
    ? "https://speak-slide-be.onrender.com" // Production backend URL
    : "", // Empty baseURL for development (uses Vite proxy)
  headers: {
    "Content-Type": "application/json",
    Accept: "application/json",
  },
  withCredentials: true, // Enable credentials
});

// Add request interceptor
api.interceptors.request.use(
  (config) => {
    // Log the request for debugging
    console.log("Request:", {
      url: config.url,
      method: config.method,
      headers: config.headers,
      data: config.data,
    });

    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add response interceptor
api.interceptors.response.use(
  (response) => {
    // Log the response for debugging
    console.log("Response:", {
      status: response.status,
      headers: response.headers,
      data: response.data,
    });
    return response;
  },
  (error) => {
    // Log the error for debugging
    console.error("Error:", {
      status: error.response?.status,
      data: error.response?.data,
      message: error.message,
    });

    if (error.response?.status === 401) {
      localStorage.removeItem("token");
      window.location.href = "/speak-slide/#/login";
    }
    return Promise.reject(error);
  }
);

export default api;
