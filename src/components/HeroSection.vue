<template>
  <section id="hero" class="bg-red-50 w-full">
    <div class="max-w-5xl mx-auto flex flex-col md:flex-row items-center justify-center px-4 sm:px-6 py-16 md:py-24 gap-8 md:gap-12 min-h-[calc(100vh-4rem)]">
      <div class="md:w-1/2 text-center md:text-left">
        <h1 class="text-3xl sm:text-4xl md:text-5xl font-extrabold text-gray-900 mb-4 md:mb-6 leading-tight">
          Transform presentations<br class="hidden sm:block" />into smart narrators
        </h1>
        <p class="text-base sm:text-lg text-gray-600 mb-6 md:mb-8 max-w-xl mx-auto md:mx-0">
          Empower your slides to talk, perfect for rehearsal, tutorial, and training needs.
        </p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
          <button class="bg-red-500 hover:bg-red-600 text-white px-6 sm:px-8 py-3 rounded-lg font-semibold text-base sm:text-lg shadow transition duration-200 focus:outline-none focus:ring-2 focus:ring-red-400 hover:scale-105 transform">Get Started</button>
          <a href="/#features" class="text-gray-700 hover:text-red-500 font-medium px-6 sm:px-8 py-3 rounded-lg border border-gray-300 hover:border-red-500 transition duration-200 text-center">Learn More</a>
        </div>
      </div>
      <div class="md:w-1/2 flex justify-center">
        <div class="relative w-full max-w-sm">
          <svg class="w-full h-auto" viewBox="0 0 180 140" fill="none">
            <rect x="10" y="20" width="140" height="90" rx="12" fill="#ef4444"/>
            <rect x="30" y="40" width="100" height="50" rx="6" fill="#fff"/>
            <circle cx="60" cy="65" r="12" fill="#ef4444"/>
            <rect x="80" y="55" width="35" height="6" rx="3" fill="#ef4444"/>
            <rect x="80" y="67" width="25" height="6" rx="3" fill="#ef4444"/>
          </svg>
          <div class="absolute -bottom-4 -right-4 w-24 h-24 bg-red-100 rounded-full opacity-50 animate-pulse"></div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
@media (max-width: 640px) {
  .min-h-\[calc\(100vh-4rem\)\] {
    min-height: calc(100vh - 4rem);
  }
}
</style> 