<template>
  <div class="navbar-wrapper">
    <header class="navbar">
      <nav class="max-w-5xl mx-auto flex items-center justify-between px-6 py-4">
        <div class="flex items-center space-x-2">
          <a href="/#hero" @click.prevent="handleNavigation('hero')" class="bg-red-500 rounded-lg p-1 hover:bg-red-600 transition-colors cursor-pointer">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#fff"/><path d="M8 8h16v12l-8 4-8-4V8z" fill="#ef4444"/><circle cx="16" cy="16" r="4" fill="#fff"/></svg>
          </a>
          <a href="/#hero" @click.prevent="handleNavigation('hero')" class="font-bold text-xl text-gray-900 hover:text-red-500 transition-colors cursor-pointer">Speak<span class="text-red-500">Slide</span></a>
        </div>
        <div class="hidden md:flex items-center space-x-8">
          <a href="/#features" @click.prevent="handleNavigation('features')" class="text-gray-700 hover:text-red-500 font-medium transition cursor-pointer">Features</a>
          <a href="/#pricing" @click.prevent="handleNavigation('pricing')" class="text-gray-700 hover:text-red-500 font-medium transition cursor-pointer">Pricing</a>
          <a href="/#contact" @click.prevent="handleNavigation('contact')" class="text-gray-700 hover:text-red-500 font-medium transition cursor-pointer">Contact</a>
          <template v-if="isAuthenticated">
            <button @click="$emit('logout')" class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-lg font-semibold shadow transition">Logout</button>
          </template>
          <template v-else>
            <router-link to="/login" class="text-gray-700 hover:text-red-500 font-medium transition">Login</router-link>
            <router-link to="/register" class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-lg font-semibold shadow transition">Register</router-link>
          </template>
        </div>
        <!-- Mobile menu button -->
        <button @click="$emit('toggle-menu')" class="md:hidden p-2 rounded-lg hover:bg-gray-100 focus:outline-none">
          <svg v-if="!showMenu" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-7 h-7 text-gray-700"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-7 h-7 text-gray-700"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
        </button>
      </nav>
      <!-- Mobile menu -->
      <transition 
        enter-active-class="transition duration-200 ease-out"
        enter-from-class="transform -translate-y-4 opacity-0"
        enter-to-class="transform translate-y-0 opacity-100"
        leave-active-class="transition duration-150 ease-in"
        leave-from-class="transform translate-y-0 opacity-100"
        leave-to-class="transform -translate-y-4 opacity-0"
      >
        <div v-if="showMenu" class="md:hidden bg-white border-t shadow-lg px-6 py-6 space-y-6">
          <a href="/#features" @click.prevent="handleNavigation('features')" class="block text-gray-700 hover:text-red-500 font-medium cursor-pointer py-2">Features</a>
          <a href="/#pricing" @click.prevent="handleNavigation('pricing')" class="block text-gray-700 hover:text-red-500 font-medium cursor-pointer py-2">Pricing</a>
          <a href="/#contact" @click.prevent="handleNavigation('contact')" class="block text-gray-700 hover:text-red-500 font-medium cursor-pointer py-2">Contact</a>
          <div class="pt-4 border-t border-gray-100">
            <template v-if="isAuthenticated">
              <button @click="$emit('logout')" class="w-full bg-red-500 hover:bg-red-600 text-white px-5 py-3 rounded-lg font-semibold shadow transition">Logout</button>
            </template>
            <template v-else>
              <router-link to="/login" class="block text-gray-700 hover:text-red-500 font-medium py-2 mb-4">Login</router-link>
              <router-link to="/register" class="w-full bg-red-500 hover:bg-red-600 text-white px-5 py-3 rounded-lg font-semibold shadow transition block text-center">Register</router-link>
            </template>
          </div>
        </div>
      </transition>
    </header>
  </div>
</template>

<script setup>
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const props = defineProps({
  showMenu: Boolean,
  isAuthenticated: Boolean
})

const handleNavigation = (sectionId) => {
  // Close mobile menu if open
  if (props.showMenu) {
    props.$emit('toggle-menu')
  }

  // If we're not on the home page, navigate to home with hash
  if (route.path !== '/') {
    router.push({ path: '/', hash: `#${sectionId}` })
    return
  }

  // If we're on the home page, scroll to section
  const element = document.getElementById(sectionId)
  if (!element) return

  // Get the navbar height
  const navbar = document.querySelector('.navbar')
  const navbarHeight = navbar ? navbar.offsetHeight : 64

  // Calculate the position
  const elementPosition = element.getBoundingClientRect().top
  const offsetPosition = elementPosition + window.scrollY - navbarHeight

  // Update URL hash
  window.location.hash = sectionId

  // Scroll to the element
  window.scrollTo({
    top: offsetPosition,
    behavior: 'smooth'
  })
}
</script>

<style scoped>
.navbar-wrapper {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
}

.navbar {
  background-color: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(8px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

a {
  scroll-behavior: smooth;
}

/* Add padding to the body to account for fixed navbar */
:deep(body) {
  padding-top: 4rem;
}

/* Improve touch targets for mobile */
@media (max-width: 768px) {
  .navbar nav {
    padding: 0.75rem 1rem;
  }
  
  button, a {
    min-height: 44px;
    display: flex;
    align-items: center;
  }
}
</style> 