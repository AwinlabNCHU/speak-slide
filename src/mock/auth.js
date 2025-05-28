// Mock user data
const users = [
  {
    id: 1,
    username: "demo",
    password: "demo123", // In a real app, this would be hashed
    email: "demo@example.com",
    role: "user",
  },
  {
    id: 2,
    username: "admin",
    password: "admin123",
    email: "admin@example.com",
    role: "admin",
  },
];

// Mock authentication functions
export const mockAuth = {
  // Mock login function
  login: async (username, password) => {
    console.log("Mock auth - Login attempt:", { username, password });
    // Simulate API delay
    await new Promise((resolve) => setTimeout(resolve, 1000));

    const user = users.find(
      (u) => u.username === username && u.password === password
    );

    console.log("Mock auth - Found user:", user);

    if (!user) {
      console.log("Mock auth - No user found");
      throw new Error("Invalid username or password");
    }

    // Create a mock JWT token
    const token = btoa(
      JSON.stringify({
        id: user.id,
        username: user.username,
        role: user.role,
        exp: Date.now() + 24 * 60 * 60 * 1000, // 24 hours from now
      })
    );

    console.log("Mock auth - Generated token");

    return {
      access_token: token,
      user: {
        id: user.id,
        username: user.username,
        email: user.email,
        role: user.role,
      },
    };
  },

  // Mock register function
  register: async (email, username, password) => {
    // Simulate API delay
    await new Promise((resolve) => setTimeout(resolve, 1000));

    // Check if username or email already exists
    if (users.some((u) => u.username === username || u.email === email)) {
      throw new Error("Username or email already exists");
    }

    const newUser = {
      id: users.length + 1,
      username,
      password,
      email,
      role: "user",
    };

    users.push(newUser);

    return {
      message: "Registration successful",
      user: {
        id: newUser.id,
        username: newUser.username,
        email: newUser.email,
        role: newUser.role,
      },
    };
  },

  // Mock verify token function
  verifyToken: (token) => {
    try {
      const decoded = JSON.parse(atob(token));
      if (decoded.exp < Date.now()) {
        throw new Error("Token expired");
      }
      return decoded;
    } catch (error) {
      throw new Error("Invalid token");
    }
  },
};
