<template>
  <section id="features" class="scroll-mt-24 h-screen flex flex-col justify-center w-full max-w-5xl px-6 mb-20">
    <h2 class="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-12">Enhance your slide presentation experience</h2>
    <div class="w-full grid grid-cols-1 md:grid-cols-2 gap-8">
      <div v-for="feature in features" :key="feature.title" class="flex items-start space-x-4 bg-white rounded-xl shadow hover:shadow-lg transition p-6 group cursor-pointer">
        <div class="bg-red-100 rounded-lg p-3 flex-shrink-0 group-hover:scale-110 transition-transform">
          <v-icon :icon="feature.icon" color="red" size="40"></v-icon>
        </div>
        <div>
          <h3 class="font-bold text-lg text-gray-900 mb-1">{{ feature.title }}</h3>
          <p class="text-gray-600 text-sm">{{ feature.desc }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup>
const props = defineProps({
  features: Array
})
</script> 