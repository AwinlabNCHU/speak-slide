<template>
  <header class="sticky top-0 z-30 bg-white/90 backdrop-blur shadow-sm">
    <nav class="max-w-5xl mx-auto flex items-center justify-between px-6 py-4">
      <div class="flex items-center space-x-2">
        <a href="#hero" class="bg-red-500 rounded-lg p-1">
          <svg width="32" height="32" viewBox="0 0 32 32" fill="none"><rect width="32" height="32" rx="8" fill="#fff"/><path d="M8 8h16v12l-8 4-8-4V8z" fill="#ef4444"/><circle cx="16" cy="16" r="4" fill="#fff"/></svg>
        </a>
        <span class="font-bold text-xl text-gray-900">Speak<span class="text-red-500">Slide</span></span>
      </div>
      <div class="hidden md:flex items-center space-x-8">
        <a href="#features" class="text-gray-700 hover:text-red-500 font-medium transition">Features</a>
        <a href="#pricing" class="text-gray-700 hover:text-red-500 font-medium transition">Pricing</a>
        <a href="#contact" class="text-gray-700 hover:text-red-500 font-medium transition">Contact</a>
        <button class="bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-lg font-semibold shadow transition animate-pulse hover:animate-none">Get Started</button>
      </div>
      <!-- Mobile menu button -->
      <button @click="$emit('toggle-menu')" class="md:hidden p-2 rounded-lg hover:bg-gray-100 focus:outline-none">
        <svg v-if="!showMenu" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-7 h-7 text-gray-700"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" /></svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-7 h-7 text-gray-700"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </nav>
    <!-- Mobile menu -->
    <transition name="fade">
      <div v-if="showMenu" class="md:hidden bg-white border-t shadow px-6 py-4 space-y-4">
        <a href="#features" class="block text-gray-700 hover:text-red-500 font-medium">Features</a>
        <a href="#pricing" class="block text-gray-700 hover:text-red-500 font-medium">Pricing</a>
        <a href="#contact" class="block text-gray-700 hover:text-red-500 font-medium">Contact</a>
        <button class="w-full bg-red-500 hover:bg-red-600 text-white px-5 py-2 rounded-lg font-semibold shadow transition">Get Started</button>
      </div>
    </transition>
  </header>
</template>

<script setup>
const props = defineProps({
  showMenu: Boolean
})
</script> 