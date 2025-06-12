<template>
  <div class="flex flex-col w-full">
    <HeroSection />
    <FeaturesSection :features="features" />
    <PricingSection />
    <ContactSection />
    <FooterSection />
  </div>
</template>

<script>
import HeroSection from './HeroSection.vue'
import FeaturesSection from './FeaturesSection.vue'
import PricingSection from './PricingSection.vue'
import ContactSection from './ContactSection.vue'
import FooterSection from './FooterSection.vue'

export default {
  name: 'Home',
  components: {
    HeroSection,
    FeaturesSection,
    PricingSection,
    ContactSection,
    FooterSection
  },
  setup() {
    const features = [
      {
        title: 'Smart Narration',
        desc: 'Transform your slides into engaging audio presentations with AI-powered narration.',
        icon: 'mdi-microphone'
      },
      {
        title: 'Multiple Languages',
        desc: 'Support for multiple languages to reach a global audience.',
        icon: 'mdi-translate'
      },
      {
        title: 'Custom Voice',
        desc: 'Choose from various voice options or use your own voice.',
        icon: 'mdi-account-voice'
      },
      {
        title: 'Easy Export',
        desc: 'Export your narrated presentations in various formats.',
        icon: 'mdi-export'
      }
    ]

    return {
      features
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
section {
  scroll-snap-align: start;
}
</style> 