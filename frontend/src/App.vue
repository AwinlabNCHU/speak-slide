<template>
  <div class="min-h-screen bg-gray-100 flex flex-col">
    <Navbar :showMenu="showMenu" @toggle-menu="showMenu = !showMenu" @navigate="currentSection = $event" />
    <transition name="fade">
      <div v-if="showMenu" class="md:hidden bg-white border-t shadow px-6 py-4 space-y-4">
        <!-- Mobile menu is handled in Navbar -->
      </div>
    </transition>
    <main class="flex-1 flex flex-col items-center justify-center">
      <section id="hero" class="h-screen flex flex-col justify-center w-full max-w-5xl bg-gray-100">
        <HeroSection />
      </section>
      <section id="features" class="scroll-mt-24 h-screen flex flex-col w-full bg-gray-50 pt-24">
        <div class="w-full max-w-5xl mx-auto px-6 mb-20">
          <h2 class="text-2xl md:text-3xl font-bold text-center text-gray-900 mb-12">
            Enhance your slide presentation experience</h2>
          <div class="w-full grid grid-cols-1 md:grid-cols-2 gap-8">
            <div v-for="feature in features" :key="feature.title" class="flex items-start space-x-4 bg-white rounded-xl shadow hover:shadow-lg transition p-6 group cursor-pointer">
              <div class="bg-red-100 rounded-lg p-3 flex-shrink-0 group-hover:scale-110 transition-transform">
                <component :is="feature.icon" class="w-10 h-10 text-red-500" />
              </div>
              <div>
                <h3 class="font-bold text-lg text-gray-900 mb-1">{{ feature.title }}</h3>
                <p class="text-gray-600 text-sm">{{ feature.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section id="pricing" class="h-screen flex flex-col justify-center w-full bg-blue-50">
        <div class="w-full max-w-6xl mx-auto">
          <PricingSection />
        </div>
      </section>
      <section id="contact" class="h-screen flex flex-col justify-center w-full bg-grey-50">
        <ContactSection />
      </section>
    </main>
    <FooterSection />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Navbar from './components/Navbar.vue'
import HeroSection from './components/HeroSection.vue'
import FeaturesSection from './components/FeaturesSection.vue'
import ContactSection from './components/ContactSection.vue'
import FooterSection from './components/FooterSection.vue'
import PricingSection from './components/PricingSection.vue'


const showMenu = ref(false)
const currentSection = ref('hero') // default section

const features = [
  {
    icon: 'mdi-file-document-outline', // or your icon component
    title: 'Slide OCR',
    desc: 'Extracts text-from octde for analysis',
  },
  {
    icon: 'mdi-file-document-outline', // or your icon component
    title: 'AI Narration',
    desc: 'Provides insightful explanations of slide content',
  },
  {
    icon: 'mdi-file-document-outline', // or your icon component
    title: 'Animation Awareness',
    desc: 'Recognizes animation order for structured prompts',
  },
  {
    icon: 'mdi-file-document-outline', // or your icon component
    title: 'Rehearsal Ready',
    desc: 'Offers smart cues for effective practice sessions',
  }
];

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
