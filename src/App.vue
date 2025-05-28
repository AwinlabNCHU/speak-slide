<template>
  <div class="min-h-screen bg-gray-100">
    <nav class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex">
            <div class="flex-shrink-0 flex items-center">
              <h1 class="text-xl font-bold">My App</h1>
            </div>
          </div>
          <div class="flex items-center">
            <template v-if="isAuthenticated">
              <button
                @click="logout"
                class="ml-4 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Logout
              </button>
            </template>
            <template v-else>
              <router-link
                to="/login"
                class="px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Login
              </router-link>
              <router-link
                to="/register"
                class="ml-4 px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700"
              >
                Register
              </router-link>
            </template>
          </div>
        </div>
      </div>
    </nav>

    <main>
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const router = useRouter()
    const isAuthenticated = ref(false)

    const checkAuth = () => {
      const token = localStorage.getItem('token')
      isAuthenticated.value = !!token
    }

    const logout = () => {
      localStorage.removeItem('token')
      isAuthenticated.value = false
      router.push('/login')
    }

    onMounted(() => {
      checkAuth()
    })

    return {
      isAuthenticated,
      logout
    }
  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
}
body {
  font-family: 'Inter', Arial, sans-serif;
}
</style>
