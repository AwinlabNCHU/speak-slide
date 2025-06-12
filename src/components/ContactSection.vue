<template>
  <section id="contact" class="bg-gray-100 w-full">
    <div class="min-h-screen flex flex-col justify-center w-full max-w-2xl mx-auto bg-white rounded-2xl shadow p-6">
      <h2 class="text-2xl font-bold text-gray-900 mb-4">Get in Touch</h2>
      <p class="text-gray-600 mb-6">Ready to transform your presentations? Contact us for a demo or more information.</p>
      <form class="flex flex-col gap-4">
        <input type="email" placeholder="Your email" class="px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-red-400" required />
        <textarea placeholder="Your message" class="px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-red-400" rows="3"></textarea>
        <button type="submit" class="bg-red-500 hover:bg-red-600 text-white px-6 py-3 rounded-lg font-semibold transition">Send Message</button>
      </form>
    </div>
  </section>
</template> 