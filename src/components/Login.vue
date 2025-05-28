<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Sign in to your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" @submit.prevent="handleSubmit">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">Username</label>
            <input
              id="username"
              v-model="username"
              name="username"
              type="text"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Username"
            />
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              name="password"
              type="password"
              required
              class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
              placeholder="Password"
            />
          </div>
        </div>

        <div>
          <button
            type="submit"
            :disabled="loading"
            class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            <span v-if="loading">Loading...</span>
            <span v-else>Sign in</span>
          </button>
        </div>

        <div v-if="error" class="text-red-500 text-center">
          {{ error }}
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import axios from 'axios'

export default {
  name: 'Login',
  setup() {
    const username = ref('')
    const password = ref('')
    const loading = ref(false)
    const error = ref('')

    const handleSubmit = async () => {
      loading.value = true
      error.value = ''

      try {
        const formData = new FormData()
        formData.append('username', username.value)
        formData.append('password', password.value)

        const response = await axios.post('http://localhost:8000/token', formData)
        const { access_token } = response.data

        // Store the token
        localStorage.setItem('token', access_token)
        
        // Redirect to home page or dashboard
        window.location.href = '/'
      } catch (err) {
        error.value = err.response?.data?.detail || 'An error occurred during login'
      } finally {
        loading.value = false
      }
    }

    return {
      username,
      password,
      loading,
      error,
      handleSubmit
    }
  }
}
</script> 