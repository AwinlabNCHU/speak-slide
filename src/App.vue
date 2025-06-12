<template>
  <div class="min-h-screen">
    <Navbar :show-menu="showMenu" @toggle-menu="toggleMenu" :is-authenticated="isAuthenticated" @logout="logout" />
    <main class="flex justify-center">
      <router-view class="w-full"></router-view>
    </main>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Navbar from './components/Navbar.vue'

export default {
  name: 'App',
  components: {
    Navbar
  },
  setup() {
    const router = useRouter()
    const isAuthenticated = ref(false)
    const showMenu = ref(false)

    const toggleMenu = () => {
      showMenu.value = !showMenu.value
    }

    const checkAuth = () => {
      const token = localStorage.getItem('token')
      isAuthenticated.value = !!token
    }

    const logout = () => {
      localStorage.removeItem('token')
      isAuthenticated.value = false
      router.push('/')
    }

    onMounted(() => {
      checkAuth()
    })

    return {
      isAuthenticated,
      logout,
      showMenu,
      toggleMenu
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
  margin: 0;
  padding: 0;
}
</style>
