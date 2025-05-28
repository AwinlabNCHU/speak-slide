<template>
  <section id="pricing" class="scroll-mt-24 w-full max-w-6xl mx-auto px-4 py-16">
    <h2 class="text-3xl md:text-4xl font-extrabold text-center text-gray-900 mb-2">You're cooking! Upgrade to keep building</h2>
    <p class="text-center text-gray-500 mb-12">Take your creativity further with more usage, more features, and the world's smartest AI.</p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div v-for="plan in plans" :key="plan.title" :class="['bg-white rounded-xl shadow p-8 flex flex-col items-center border', plan.suggested ? 'border-blue-500 relative' : 'border-gray-200']">
        <div v-if="plan.suggested" class="absolute -top-4 left-1/2 -translate-x-1/2 bg-blue-500 text-white text-xs font-bold px-3 py-1 rounded-full shadow">SUGGESTED</div>
        <h3 class="text-lg font-bold mb-2">{{ plan.title }}</h3>
        <div class="text-3xl text-black font-extrabold mb-1">US${{ plan.price }}<span class="text-base font-medium text-gray-500">/month</span></div>
        <ul class="text-gray-700 text-sm mb-6 space-y-1">
          <li v-for="(feature, i) in plan.features" :key="i" class="flex items-center gap-2">
            <span class="text-green-500">✔</span> {{ feature }}
          </li>
        </ul>
        <button :class="plan.buttonClass + ' w-full py-2 rounded font-semibold text-white transition'">{{ plan.buttonText }}</button>
      </div>
    </div>
  </section>
</template>

<script setup>
const plans = [
  {
    title: 'Free',
    price: 0,
    features: [
      'Unlimited free model generations',
      '5 standard generations per day',
    ],
    buttonText: 'Get Started',
    buttonClass: 'bg-blue-600 hover:bg-blue-700',
  },
  {
    title: 'Starter',
    price: 10,
    features: [
      'Unlimited free model generations',
      '100 standard generations per day',
      'Access to premium models',
    ],
    buttonText: 'Choose Basic',
    buttonClass: 'bg-purple-600 hover:bg-purple-700',
  },
  {
    title: 'Pro',
    price: 30,
    features: [
      'Unlimited free model generations',
      '300 standard generations per day',
      'Access to premium models',
      'Private and Unlisted Projects',
    ],
    buttonText: 'Choose Pro',
    buttonClass: 'bg-green-500 hover:bg-green-600',
    suggested: true,
  },
  {
    title: 'Max',
    price: 60,
    features: [
      'Unlimited free model generations',
      '600 standard generations per day',
      'Access to premium models',
      'Private and Unlisted Projects',
    ],
    buttonText: 'Choose Max',
    buttonClass: 'bg-pink-500 hover:bg-pink-600',
  },
]
</script> 