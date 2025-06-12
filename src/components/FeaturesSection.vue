<template>
  <section id="features" class="scroll-mt-16 bg-white w-full py-16 md:py-24">
    <div class="w-full max-w-5xl mx-auto px-4 sm:px-6">
      <h2 class="text-2xl sm:text-3xl md:text-4xl font-bold text-center text-gray-900 mb-8 md:mb-16">Enhance your slide presentation experience</h2>
      <div class="w-full grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6 md:gap-8">
        <div v-for="feature in features" :key="feature.title" 
          class="flex items-start space-x-4 bg-white rounded-xl shadow-sm hover:shadow-lg transition-all duration-300 p-4 sm:p-6 group cursor-pointer border border-gray-100 hover:border-red-100">
          <div class="bg-red-50 rounded-lg p-2 sm:p-3 flex-shrink-0 group-hover:scale-110 transition-transform duration-300">
            <v-icon :icon="feature.icon" color="red" size="32" class="sm:w-10 sm:h-10"></v-icon>
          </div>
          <div class="flex-1">
            <h3 class="font-bold text-base sm:text-lg text-gray-900 mb-1 sm:mb-2">{{ feature.title }}</h3>
            <p class="text-gray-600 text-sm sm:text-base leading-relaxed">{{ feature.desc }}</p>
          </div>
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

<style scoped>
@media (max-width: 640px) {
  .scroll-mt-16 {
    scroll-margin-top: 4rem;
  }
}
</style> 