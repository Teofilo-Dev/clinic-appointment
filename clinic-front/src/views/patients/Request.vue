<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50 overflow-hidden relative">
    <!-- Animated Background Blobs -->
    <div class="fixed inset-0 z-0 overflow-hidden pointer-events-none">
      <Teleport to="body">
        <div class="fixed inset-0 z-0 overflow-hidden pointer-events-none">
          <div
            class="absolute -top-40 -right-40 w-80 h-80 bg-gradient-to-br from-blue-300 to-blue-200 rounded-full blur-3xl opacity-20 animate-blob"
          />
          <div
            class="absolute -bottom-40 -left-40 w-80 h-80 bg-gradient-to-br from-emerald-300 to-emerald-200 rounded-full blur-3xl opacity-20 animate-blob-delayed"
          />
        </div>
      </Teleport>
    </div>

    <!-- Fixed Navigation -->
    <nav class="fixed top-0 left-0 right-0 z-50 backdrop-blur-xl border-b border-white/10 animate-slide-down" style="background: linear-gradient(to right, #3b6fd4, #10d9a0);">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 sm:py-4 flex justify-between items-center">
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 sm:w-10 sm:h-10 rounded-lg bg-white flex items-center justify-center" style="background:white;">
            <svg class="w-5.5 h-5.5 sm:w-6 sm:h-6" viewBox="0 0 24 24" fill="none">
              <defs>
                <linearGradient id="logoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#3b6fd4" />
                  <stop offset="100%" stop-color="#10d9a0" />
                </linearGradient>
              </defs>
              <rect x="10" y="4" width="4" height="16" rx="1.5" fill="url(#logoGrad)" />
              <rect x="4" y="10" width="16" height="4" rx="1.5" fill="url(#logoGrad)" />
            </svg>
          </div>
          <span class="font-bold text-base sm:text-lg text-white">MagsCare</span>
        </div>
        <!-- Desktop nav -->
        <div class="hidden md:flex gap-6 lg:gap-8">
          <a
            v-for="item in navItems"
            :key="item.name"
            :href="item.link"
            class="text-white/90 hover:text-white font-medium transition-colors hover:scale-105 text-sm lg:text-base"
          >
            {{ item.name }}
          </a>
        </div>
        <div class="flex items-center gap-2 sm:gap-3">
          <button @click="openBookingModal()" class="px-4 sm:px-6 py-2 bg-white rounded-lg font-semibold hover:shadow-lg transition-all hover:scale-105 cursor-pointer text-sm sm:text-base" style="color: #3b6fd4;">
            Book Now
          </button>
          <!-- Mobile hamburger -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden w-9 h-9 flex flex-col items-center justify-center gap-1.5 rounded-lg bg-white/20 hover:bg-white/30 transition cursor-pointer" aria-label="Toggle menu">
            <span :class="['block w-5 h-0.5 bg-white transition-all duration-300', mobileMenuOpen ? 'rotate-45 translate-y-2' : '']"></span>
            <span :class="['block w-5 h-0.5 bg-white transition-all duration-300', mobileMenuOpen ? 'opacity-0' : '']"></span>
            <span :class="['block w-5 h-0.5 bg-white transition-all duration-300', mobileMenuOpen ? '-rotate-45 -translate-y-2' : '']"></span>
          </button>
        </div>
      </div>
      <!-- Mobile menu dropdown -->
      <div v-if="mobileMenuOpen" class="md:hidden border-t border-white/20 px-4 pb-4" style="background: linear-gradient(to right, #3b6fd4, #10d9a0);">
        <div class="flex flex-col gap-1 pt-2">
          <a
            v-for="item in navItems"
            :key="item.name"
            :href="item.link"
            class="text-white hover:text-white font-medium py-2.5 px-3 rounded-lg hover:bg-white/20 transition-colors"
            @click="mobileMenuOpen = false"
          >
            {{ item.name }}
          </a>
        </div>
      </div>
    </nav>

    <div class="relative z-10 pt-24">
      <!-- Hero Section -->
      <section class="min-h-screen flex items-center justify-center px-4 sm:px-6 lg:px-8 py-16 sm:py-20">
        <div class="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-12 items-center w-full">
          <!-- Left Content -->
          <div class="space-y-6 sm:space-y-8 animate-fade-in text-center lg:text-left">
            <div class="inline-block px-3 sm:px-4 py-1.5 sm:py-2 bg-blue-100 text-blue-700 rounded-full text-xs sm:text-sm font-semibold animate-slide-right" style="animation-delay: 0.1s">
              Welcome to Mags Clinic Centre
            </div>

            <h1 class="text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-bold text-slate-900 leading-tight animate-slide-right" style="animation-delay: 0.2s">
              Your Health <br />
              <span class="bg-gradient-to-r from-blue-500 via-emerald-500 to-blue-600 bg-clip-text text-transparent">
                Matters Most
              </span>
            </h1>

            <p class="text-base sm:text-lg lg:text-xl text-slate-600 leading-relaxed max-w-lg mx-auto lg:mx-0 animate-slide-right" style="animation-delay: 0.3s">
              Your trusted Mags clinic, now completely digital. Skip the waiting room — book expert medical care and view real-time doctor schedules instantly.
            </p>

            <div class="flex flex-col sm:flex-row gap-3 sm:gap-4 animate-slide-right justify-center lg:justify-start" style="animation-delay: 0.4s">
              <button @click="openBookingModal()" class="px-6 sm:px-8 py-3 sm:py-4 bg-gradient-to-r from-blue-500 to-emerald-500 text-white rounded-xl font-bold text-base sm:text-lg hover:shadow-xl transition-all flex items-center justify-center gap-2 hover:scale-105 cursor-pointer">
                Book Appointment
                <svg class="w-4 h-4 sm:w-5 sm:h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </button>
              <a href="#footer" class="px-6 sm:px-8 py-3 sm:py-4 border-2 border-blue-500 text-blue-600 rounded-xl font-bold text-base sm:text-lg hover:bg-blue-50 transition-all hover:scale-105 flex items-center justify-center">
                Contact Us
              </a>
            </div>

            <!-- Stats -->
            <div class="grid grid-cols-3 gap-2 sm:gap-6 pt-4 sm:pt-8">
              <div v-for="(stat, idx) in stats" :key="idx" class="text-center" :style="{ animationDelay: `${0.5 + idx * 0.1}s` }">
                <div class="text-2xl sm:text-3xl lg:text-4xl font-bold bg-gradient-to-r from-blue-500 to-emerald-500 bg-clip-text text-transparent">
                  <span v-if="statsVisible">{{ stat.value }}{{ stat.suffix }}</span>
                </div>
                <p class="text-slate-600 text-xs sm:text-sm mt-1 sm:mt-2">{{ stat.label }}</p>
              </div>
            </div>
          </div>

          <!-- 3D Card with Enhanced Animations -->
          <div class="relative h-72 sm:h-96 lg:h-[500px] animate-scale-in mx-4 sm:mx-8 lg:mx-0">
            <div
              class="absolute inset-0 bg-gradient-to-br from-blue-400 to-emerald-400 rounded-3xl shadow-2xl animate-float"
              style="filter: blur(40px); opacity: 0.3"
            />
            <div
              class="absolute inset-4 sm:inset-0 rounded-3xl shadow-2xl overflow-hidden group hover:shadow-2xl transition-all hover:scale-105 duration-500 flex flex-col justify-center items-center text-white"
              style="perspective: 1200px"
            >
              <!-- Doctor Background Image -->
              <img
                src="https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&q=80&w=800&h=600"
                alt="Doctor"
                class="absolute inset-0 w-full h-full object-cover transition-transform duration-500 group-hover:scale-110"
              />
              <!-- Dark Overlay for Contrast -->
              <div class="absolute inset-0 bg-gradient-to-t from-slate-950/80 via-slate-950/30 to-transparent opacity-85 z-0"></div>
              
              <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent animate-shine z-0" />

              <h3 class="text-2xl sm:text-3xl lg:text-4xl font-extrabold text-center relative z-10 font-sans tracking-wide">Mags Magscare</h3>
              <p class="text-center mt-2 sm:mt-3 text-white/90 text-sm sm:text-lg relative z-10 font-medium">Expert care at your fingertips</p>

              <div
                class="absolute top-4 sm:top-6 left-4 sm:left-6 bg-white/20 backdrop-blur px-3 sm:px-4 py-1.5 sm:py-2 rounded-full border border-white/30 z-20 animate-float"
                style="animation-delay: 0.3s"
              >
                <p class="text-xs sm:text-sm font-semibold text-white">Verified & Trusted</p>
              </div>
            </div>

            <!-- Floating Elements — hidden on small screens to prevent overflow -->
            <div class="hidden sm:block absolute -top-6 -right-6 lg:-top-8 lg:-right-8 w-24 h-24 lg:w-32 lg:h-32 bg-blue-100 rounded-2xl p-3 lg:p-4 text-blue-600 shadow-xl animate-float" style="animation-delay: 0.2s">
              <div class="flex flex-col items-center justify-center h-full">
                <svg class="w-6 h-6 lg:w-8 lg:h-8 fill-current mb-1 lg:mb-2" viewBox="0 0 24 24">
                  <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z" />
                </svg>
                <p class="text-xs font-bold text-center">4.9 Rating</p>
              </div>
            </div>

            <div class="hidden sm:block absolute -bottom-6 -left-6 lg:-bottom-8 lg:-left-8 w-24 h-24 lg:w-32 lg:h-32 bg-emerald-100 rounded-2xl p-3 lg:p-4 text-emerald-600 shadow-xl animate-float" style="animation-delay: 0.4s">
              <div class="flex flex-col items-center justify-center h-full">
                <svg class="w-6 h-6 lg:w-8 lg:h-8 mb-1 lg:mb-2 fill-current" viewBox="0 0 24 24">
                  <path d="M12 2c-4.97 0-9 4.03-9 9v7c0 1.66 1.34 3 3 3h3v-8H5v-2c0-3.87 3.13-7 7-7s7 3.13 7 7v2h-4v8h3c1.66 0 3-1.34 3-3v-7c0-4.97-4.03-9-9-9z"/>
                </svg>
                <p class="text-xs font-bold text-center">24/7 Support</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Services Section -->
      <section id="services" class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 bg-white/50 backdrop-blur">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-12 sm:mb-20 reveal-on-scroll reveal-fade-up">
            <span class="inline-block px-3 sm:px-4 py-1.5 sm:py-2 bg-blue-100 text-blue-700 rounded-full text-xs sm:text-sm font-semibold mb-3 sm:mb-4">
              Our Services
            </span>
            <h2 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-bold text-slate-900 mb-4 sm:mb-6">Comprehensive Care Solutions</h2>
            <p class="text-base sm:text-lg lg:text-xl text-slate-600 max-w-2xl mx-auto">
              Everything you need for optimal health and wellness in one place
            </p>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 reveal-stagger-grid">
            <div
              v-for="(service, idx) in services"
              :key="idx"
              class="group bg-white/80 backdrop-blur border border-slate-200 rounded-2xl p-8 cursor-pointer hover:border-blue-400 transition-all hover:shadow-lg hover:-translate-y-3 relative overflow-hidden reveal-on-scroll reveal-fade-up"
              :style="{ transitionDelay: `${idx * 0.12}s` }"
              @click="openBookingModal()"
            >
              <div class="relative z-10 space-y-4">
                <!-- Render inline HTML SVGs to prevent component loading issues -->
                <div class="w-14 h-14 bg-gradient-to-br from-blue-100 to-emerald-100 rounded-xl flex items-center justify-center text-blue-600 mb-6 group-hover:scale-115 group-hover:rotate-12 transition-all" v-html="service.icon"></div>

                <h3 class="text-xl font-bold text-slate-900">{{ service.title }}</h3>
                <p class="text-slate-600">{{ service.description }}</p>

                <ul class="space-y-2">
                  <li v-for="feature in service.features" :key="feature" class="text-sm text-slate-600 flex items-center gap-2">
                    <svg class="w-4 h-4 text-emerald-500" fill="currentColor" viewBox="0 0 20 20">
                      <path
                        fill-rule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                        clip-rule="evenodd"
                      />
                    </svg>
                    {{ feature }}
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- How It Works -->
      <section id="how-it-works" class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-12 sm:mb-20 reveal-on-scroll reveal-fade-up">
            <span class="inline-block px-3 sm:px-4 py-1.5 sm:py-2 bg-emerald-100 text-emerald-700 rounded-full text-xs sm:text-sm font-semibold mb-3 sm:mb-4">
              Simple Process
            </span>
            <h2 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-bold text-slate-900 mb-4 sm:mb-6">Book in 3 Easy Steps</h2>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div
              v-for="(step, idx) in steps"
              :key="idx"
              class="relative text-center group hover:-translate-y-2 transition-all reveal-on-scroll reveal-scale-in"
              :style="{ transitionDelay: `${idx * 0.18}s` }"
            >
              <div
                class="w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-emerald-500 flex items-center justify-center text-white text-3xl font-bold mx-auto mb-6 shadow-lg group-hover:shadow-xl group-hover:scale-110 transition-all"
              >
                {{ step.num }}
              </div>
              <h3 class="text-2xl font-bold text-slate-900 mb-2">{{ step.title }}</h3>
              <p class="text-slate-600">{{ step.desc }}</p>

              <div
                v-if="idx < 2"
                class="hidden md:block absolute top-10 -right-4 w-8 h-1 bg-gradient-to-r from-blue-500 to-emerald-500"
              />
            </div>
          </div>
        </div>
      </section>

      <!-- Doctors Section -->
      <section id="doctors" class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-blue-50 to-emerald-50">
        <div class="max-w-6xl mx-auto">
          <div class="text-center mb-12 sm:mb-20 reveal-on-scroll reveal-fade-up">
            <span class="inline-block px-3 sm:px-4 py-1.5 sm:py-2 bg-blue-100 text-blue-700 rounded-full text-xs sm:text-sm font-semibold mb-3 sm:mb-4">
              Expert Team
            </span>
            <h2 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-bold text-slate-900 mb-4 sm:mb-6">Meet Our Doctors</h2>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div
              v-for="doctor in displayedDoctors"
              :key="doctor.id"
              class="group bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition-all hover:-translate-y-3 relative reveal-on-scroll reveal-slide-left cursor-pointer"
              :style="{ transitionDelay: `${(doctor.id - 1) * 0.14}s` }"
              @click="openBookingModal(doctor.id)"
            >
              <!-- Header with Image Source -->
              <div class="h-48 relative overflow-hidden">
                <img
                  :src="doctor.image"
                  :alt="doctor.name"
                  class="w-full h-full object-cover object-center transition-transform duration-500 group-hover:scale-110"
                />
                <!-- Gradient overlay to keep it sleek and clinical -->
                <div class="absolute inset-0 bg-gradient-to-t from-slate-900/50 via-transparent to-transparent opacity-60"></div>
                <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent animate-shine" />
              </div>

              <div class="px-6 pb-8 pt-2 relative z-10">
                <!-- Avatar Circle with original Letter (dont remove the letters) -->
                <div
                  :class="`w-20 h-20 rounded-full bg-gradient-to-br ${doctor.color} mx-auto -mt-12 mb-4 flex items-center justify-center text-white text-2xl font-bold border-4 border-white shadow-lg group-hover:scale-115 group-hover:rotate-10 transition-all animate-float relative z-20`"
                >
                  {{ doctor.name.replace('Dr. ', '').charAt(0) }}
                </div>

                <h3 class="text-xl font-bold text-slate-900 text-center mb-1">{{ doctor.name }}</h3>
                <p class="text-blue-600 text-sm text-center font-semibold mb-6">{{ doctor.specialty }}</p>

                <!-- Stats -->
                <div class="space-y-3">
                  <div class="flex items-center justify-center gap-2 text-sm text-slate-600 transition-transform">
                    <svg class="w-4 h-4 text-yellow-500 fill-current" viewBox="0 0 20 20">
                      <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" />
                    </svg>
                    <span class="font-semibold">{{ doctor.rating }} rating</span>
                  </div>

                  <div class="flex items-center justify-center gap-2 text-sm text-slate-600 transition-transform">
                    <svg class="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM9 12a6 6 0 11-12 0 6 6 0 0112 0z" />
                    </svg>
                    <span>{{ doctor.patients }} patients</span>
                  </div>

                  <div class="flex items-center justify-center gap-2 text-sm text-slate-600 transition-transform">
                    <svg class="w-4 h-4 text-emerald-500" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z" />
                    </svg>
                    <span>{{ doctor.experience }} years exp.</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Testimonials -->

      <!-- CTA Section -->
      <section class="py-16 sm:py-24 px-4 sm:px-6 lg:px-8 bg-gradient-to-r from-blue-500 to-emerald-500">
        <div class="max-w-4xl mx-auto text-center reveal-on-scroll reveal-scale-in">
          <h2 class="text-3xl sm:text-4xl lg:text-5xl xl:text-6xl font-bold text-white mb-4 sm:mb-6">Ready to Book Your Appointment?</h2>
          <p class="text-base sm:text-lg lg:text-xl text-white/90 mb-6 sm:mb-8">Join thousands of satisfied patients who trust us with their Magscare needs</p>
          <button @click="openBookingModal()" class="px-8 sm:px-10 py-3 sm:py-4 bg-white text-blue-600 rounded-xl font-bold text-base sm:text-lg hover:shadow-xl transition-all hover:scale-105 cursor-pointer">
            Get Started Now
          </button>
        </div>
      </section>

      <!-- Footer -->
      <footer id="footer" class="bg-slate-900 text-white py-12 sm:py-16 px-4 sm:px-6 lg:px-8">
        <div class="max-w-6xl mx-auto grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8 sm:gap-10 lg:gap-12 mb-8 sm:mb-12">
          <div class="sm:col-span-2 lg:col-span-1">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-emerald-500 flex items-center justify-center">
                <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none">
                  <rect x="10" y="4" width="4" height="16" rx="1.5" fill="white" />
                  <rect x="4" y="10" width="16" height="4" rx="1.5" fill="white" />
                </svg>
              </div>
              <span class="font-bold text-lg">MagsCare</span>
            </div>
            <p class="text-slate-400 text-sm sm:text-base">Your trusted Magscare partner for quality medical services and expert care.</p>
          </div>

          <div>
            <h4 class="font-bold mb-3 sm:mb-4 text-base sm:text-lg">Quick Links</h4>
            <ul class="space-y-2 text-slate-400 text-sm sm:text-base">
              <li><a href="#services" class="hover:text-white transition">Services</a></li>
              <li><a href="#doctors" class="hover:text-white transition">Doctors</a></li>
              <li><a href="#testimonials" class="hover:text-white transition">About Us</a></li>
            </ul>
          </div>

          <div>
            <h4 class="font-bold mb-3 sm:mb-4 text-base sm:text-lg">Contact</h4>
            <ul class="space-y-2 text-slate-400 text-sm sm:text-base">
              <li class="flex items-center gap-2">📞 +1 (555) 123-4567</li>
              <li class="flex items-center gap-2">📧 info@Magscare.com</li>
              <li class="flex items-center gap-2">📍 123 Medical Ave</li>
            </ul>
          </div>

          <div>
            <h4 class="font-bold mb-3 sm:mb-4 text-base sm:text-lg">Hours</h4>
            <p class="text-slate-400 text-sm sm:text-base">Monday - Friday: 8am - 6pm<br />Saturday: 9am - 4pm<br />Sunday: Closed</p>
          </div>
        </div>

        <div class="border-t border-slate-700 pt-6 sm:pt-8 text-center text-slate-400 text-sm sm:text-base">
          <p>&copy; 2026 MagsCare Pro. All rights reserved.</p>
        </div>
      </footer>
    </div>

    <!-- Stunning Glassmorphic 3D Booking Modal -->
    <Teleport to="body">
      <div
        v-if="isBookingModalOpen"
        class="fixed inset-0 z-[100] flex items-end sm:items-center justify-center p-0 sm:p-4 bg-slate-950/60 backdrop-blur-md transition-opacity duration-300"
        @click.self="closeBookingModal"
      >
        <div
          class="relative w-full max-w-lg bg-white/90 backdrop-blur-xl border border-white/40 shadow-2xl rounded-t-3xl sm:rounded-3xl p-5 sm:p-6 lg:p-8 overflow-hidden transform transition-all duration-500 scale-100 hover:shadow-3xl animate-scale-in max-h-[90dvh] overflow-y-auto"
          style="perspective: 1200px"
        >
          <!-- Floating decorative bubble in background of modal -->
          <div class="absolute -top-10 -right-10 w-32 h-32 bg-blue-400/20 rounded-full blur-xl pointer-events-none" />

          <!-- Modal Header -->
          <div class="flex justify-between items-center mb-6 relative z-10">
            <div>
              <h3 class="text-2xl font-bold text-slate-900">Request Appointment</h3>
              <p class="text-sm text-slate-500 mt-1">Fill out the form to reserve your slot.</p>
            </div>
            <button
              @click="closeBookingModal"
              class="w-10 h-10 rounded-full bg-slate-100 hover:bg-slate-200 flex items-center justify-center text-slate-700 transition cursor-pointer"
            >
              ✕
            </button>
          </div>

          <!-- Success State -->
          <div v-if="successMsg" class="py-8 text-center space-y-4 animate-scale-in">
            <div class="w-16 h-16 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mx-auto shadow-lg animate-pulse-custom">
              <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
              </svg>
            </div>
            <h4 class="text-xl font-bold text-slate-900">Request Received!</h4>
            <p class="text-slate-600 leading-relaxed max-w-sm mx-auto">
              {{ successMsg }}
            </p>
            <button
              @click="closeBookingModal"
              class="px-8 py-3 bg-gradient-to-r from-blue-500 to-emerald-500 text-white font-bold rounded-xl shadow-md hover:shadow-lg transition hover:scale-105 cursor-pointer"
            >
              Done
            </button>
          </div>

          <!-- Form State -->
          <form v-else @submit.prevent="submitRequest" class="space-y-4 relative z-10" novalidate>
            <!-- Full Name -->
            <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.name }">
              <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Full Name</label>
              <input
                type="text"
                v-model="fullName"
                placeholder="Jane Rivera"
                class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
              />
            </div>

            <!-- Email & Phone -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.email }">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Email</label>
                <input
                  type="email"
                  v-model="formData.email"
                  placeholder="jane@email.com"
                  class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
                />
              </div>
              <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.phone }">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Phone</label>
                <input
                  type="tel"
                  v-model="formData.phone"
                  placeholder="(555) 123-4567"
                  class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
                />
              </div>
            </div>

            <!-- Doctor Dropdown -->
            <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.doctor_id }">
              <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Doctor</label>
              <select
                v-model="formData.doctor_id"
                class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition cursor-pointer focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
              >
                <option :value="null" disabled>
                  {{ loadingDoctors ? 'Loading doctors list...' : 'Select your doctor' }}
                </option>
                <option v-for="doc in displayedDoctors" :key="doc.id" :value="doc.id">
                  {{ doc.name }} — {{ doc.specialty }}
                </option>
              </select>
            </div>

            <!-- Date & Time -->
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.date }">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Preferred Date</label>
                <input
                  type="date"
                  v-model="formData.date"
                  class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
                />
              </div>
              <div class="flex flex-col gap-1.5" :class="{ 'field-error': errors.time }">
                <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Preferred Time</label>
                <input
                  type="time"
                  v-model="formData.time"
                  class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
                />
              </div>
            </div>

            <!-- Notes -->
            <div class="flex flex-col gap-1.5">
              <label class="text-xs font-bold text-slate-700 uppercase tracking-wider">Notes for Care Team (Optional)</label>
              <textarea
                v-model="formData.reason"
                placeholder="Anything we should know before your visit..."
                class="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-xl outline-none text-slate-900 transition resize-none h-20 focus:bg-white focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
              ></textarea>
            </div>

            <!-- Error Alerts -->
            <div v-if="errorMsg" class="p-3 bg-rose-50 border border-rose-200 text-rose-600 text-sm font-semibold rounded-xl flex items-center gap-2 animate-shake">
              <span>⚠️</span>
              <span>{{ errorMsg }}</span>
            </div>

            <!-- Submit Button -->
            <button
              type="submit"
              class="w-full py-4 mt-2 bg-gradient-to-r from-blue-500 to-emerald-500 text-white font-bold text-lg rounded-xl shadow-lg hover:shadow-xl hover:scale-[1.02] active:scale-95 transition flex items-center justify-center gap-2 cursor-pointer"
              :disabled="loading"
            >
              <span v-if="loading" class="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin"></span>
              <span v-else>Request Appointment</span>
            </button>
          </form>
        </div>
      </div>
    </Teleport>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import { getDoctors, requestAppointment } from '@services/api';

const mobileMenuOpen = ref(false);

const isBookingModalOpen = ref(false);
const successMsg = ref('');
const errorMsg = ref('');
const loading = ref(false);
const loadingDoctors = ref(false);

const fullName = ref('');
const formData = ref({
  email: '',
  phone: '',
  doctor_id: null as number | null,
  date: '',
  time: '',
  reason: '',
});

const errors = ref({
  name: false,
  email: false,
  phone: false,
  doctor_id: false,
  date: false,
  time: false,
});

const statsVisible = ref(false);
const navItems = [
  { name: 'Services', link: '#services' },
  { name: 'How It Works', link: '#how-it-works' },
  { name: 'Doctors', link: '#doctors' },
];

interface DBDoctor {
  id: number;
  name: string;
  specialty: string;
  rating: number;
  patients: number;
  experience: number;
  color: string;
  image: string;
}

const dbDoctors = ref<DBDoctor[]>([]);

const fallbackDoctors: DBDoctor[] = [
  { id: 1, name: 'Dr. Sarah Johnson', specialty: 'General Practice', rating: 4.9, patients: 2340, experience: 12, color: 'from-blue-500 to-blue-600', image: 'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&crop=faces&q=80&w=400&h=300' },
  { id: 2, name: 'Dr. Michael Chen', specialty: 'Cardiology', rating: 4.8, patients: 1890, experience: 15, color: 'from-emerald-500 to-emerald-600', image: 'https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&crop=faces&q=80&w=400&h=300' },
  { id: 3, name: 'Dr. Emily Rodriguez', specialty: 'Pediatrics', rating: 4.9, patients: 2100, experience: 10, color: 'from-rose-500 to-rose-600', image: 'https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&crop=faces&q=80&w=400&h=300' },
  { id: 4, name: 'Dr. James Wilson', specialty: 'Orthopedics', rating: 4.7, patients: 1650, experience: 18, color: 'from-purple-500 to-purple-600', image: 'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&crop=faces&q=80&w=400&h=300' },
];

const displayedDoctors = computed(() => {
  return dbDoctors.value.length > 0 ? dbDoctors.value : fallbackDoctors;
});

const services = [
  { 
    icon: `<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>`,
    title: 'General Checkup', 
    description: 'Comprehensive health screening', 
    features: ['Full body scan', 'Blood work', 'Health report'] 
  },
  { 
    icon: `<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" /></svg>`,
    title: 'Specialist Care', 
    description: 'Expert specialists available', 
    features: ['Expert teams', 'Advanced tech', 'Proven results'] 
  },
  { 
    icon: `<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>`,
    title: 'Prescriptions', 
    description: 'Quick medication prescribing', 
    features: ['Digital prescriptions', 'Home delivery', 'Refills online'] 
  },
  { 
    icon: `<svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M14.828 14.828a4 4 0 01-5.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>`,
    title: 'Dental Health', 
    description: 'Complete dental services', 
    features: ['Cleaning', 'Whitening', 'Emergency care'] 
  },
];

const steps = [
  { num: 1, title: 'Select Doctor', desc: 'Choose from our expert specialists' },
  { num: 2, title: 'Pick Time Slot', desc: 'Select your preferred appointment time' },
  { num: 3, title: 'Confirm Booking', desc: 'Complete your appointment reservation' },
];

const testimonials = [
  { name: 'Alice Thompson', role: 'Patient', comment: 'Professional, caring, and incredibly convenient. Best Magscare experience I\'ve had!', rating: 5 },
  { name: 'Robert Johnson', role: 'Patient', comment: 'The appointment booking process was seamless and the doctor was very attentive.', rating: 5 },
  { name: 'Maria Garcia', role: 'Patient', comment: 'Excellent service and world-class doctors. I\'ll definitely recommend to friends!', rating: 5 },
];

const stats = [
  { value: 550, label: 'Happy Patients', suffix: '+' },
  { value: 7, label: 'Expert Doctors', suffix: '+' },
  { value: 24, label: 'Support', suffix: '/7' },
];

async function loadDoctors() {
  loadingDoctors.value = true;
  try {
    const res = await getDoctors();
    const colors = [
      'from-blue-500 to-blue-600',
      'from-emerald-500 to-emerald-600',
      'from-rose-500 to-rose-600',
      'from-purple-500 to-purple-600',
    ];
    const doctorImages = [
      'https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&crop=faces&q=80&w=400&h=300',
      'https://images.unsplash.com/photo-1537368910025-700350fe46c7?auto=format&fit=crop&crop=faces&q=80&w=400&h=300',
      'https://images.unsplash.com/photo-1594824476967-48c8b964273f?auto=format&fit=crop&crop=faces&q=80&w=400&h=300',
      'https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?auto=format&fit=crop&crop=faces&q=80&w=400&h=300',
    ];
    dbDoctors.value = res.data.map((d: any, index: number) => ({
      id: d.id,
      name: `Dr. ${d.user.first_name} ${d.user.last_name}`,
      specialty: d.specialization,
      rating: 4.9,
      patients: 1200 + (d.id * 142) % 800,
      experience: 6 + (d.id * 4) % 15,
      color: colors[index % colors.length],
      image: doctorImages[index % doctorImages.length],
    }));
  } catch (err) {
    console.error('Could not load doctors from database:', err);
  } finally {
    loadingDoctors.value = false;
  }
}

function openBookingModal(doctorId: number | null = null) {
  errorMsg.value = '';
  successMsg.value = '';
  if (doctorId !== null) {
    formData.value.doctor_id = doctorId;
  } else {
    formData.value.doctor_id = null;
  }
  isBookingModalOpen.value = true;
}

function closeBookingModal() {
  isBookingModalOpen.value = false;
}

function validateForm() {
  errors.value = {
    name: !fullName.value.trim() || fullName.value.trim().split(/\s+/).length < 2,
    email: !formData.value.email.trim() || !formData.value.email.includes('@'),
    phone: !formData.value.phone.trim(),
    doctor_id: !formData.value.doctor_id,
    date: !formData.value.date.trim(),
    time: !formData.value.time.trim(),
  };
  return !Object.values(errors.value).some(Boolean);
}

async function submitRequest() {
  errorMsg.value = '';
  successMsg.value = '';

  if (!validateForm()) {
    if (fullName.value.trim() && fullName.value.trim().split(/\s+/).length < 2) {
      errorMsg.value = 'Please enter both your first and last name.';
    } else {
      errorMsg.value = 'Please fill out all required fields correctly.';
    }
    return;
  }

  loading.value = true;
  try {
    const nameParts = fullName.value.trim().split(/\s+/);
    const first_name = nameParts[0] || '';
    const last_name = nameParts.slice(1).join(' ') || '.';

    const localDateTimeStr = `${formData.value.date}T${formData.value.time}:00`;
    const appointment_date = new Date(localDateTimeStr).toISOString();

    const payload = {
      first_name,
      last_name,
      email: formData.value.email,
      phone: formData.value.phone,
      doctor_id: formData.value.doctor_id,
      appointment_date,
      reason: formData.value.reason,
    };

    await requestAppointment(payload);
    successMsg.value = 'Your appointment request has been received! We will confirm your exact time by email shortly.';
    
    // Clear fields
    fullName.value = '';
    formData.value = {
      email: '',
      phone: '',
      doctor_id: null,
      date: '',
      time: '',
      reason: '',
    };
  } catch (err: any) {
    errorMsg.value = err.response?.data?.error || 'An error occurred. Please try again.';
  } finally {
    loading.value = false;
  }
}

onMounted(() => {
  loadDoctors();
  setTimeout(() => {
    statsVisible.value = true;
  }, 100);

  // Scroll-reveal using IntersectionObserver — repeats every time section is scrolled into view
  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        } else {
          // Remove so it animates again next time the user scrolls back
          entry.target.classList.remove('is-visible');
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -60px 0px' }
  );

  document.querySelectorAll('.reveal-on-scroll').forEach((el) => {
    revealObserver.observe(el);
  });
});
</script>

<style scoped>
/* ========== Scroll Reveal Animations ========== */

/* Base hidden state for all reveal elements */
.reveal-on-scroll {
  opacity: 0;
  will-change: opacity, transform;
  transition: opacity 0.7s cubic-bezier(0.22, 1, 0.36, 1),
              transform 0.7s cubic-bezier(0.22, 1, 0.36, 1);
}

/* Fade + slide up */
.reveal-fade-up {
  transform: translateY(48px);
}
.reveal-fade-up.is-visible {
  opacity: 1;
  transform: translateY(0);
}

/* Slide in from the left */
.reveal-slide-left {
  transform: translateX(-40px);
}
.reveal-slide-left.is-visible {
  opacity: 1;
  transform: translateX(0);
}

/* Scale + fade in */
.reveal-scale-in {
  transform: scale(0.88);
}
.reveal-scale-in.is-visible {
  opacity: 1;
  transform: scale(1);
}
/* ============================================= */
@keyframes float {
  0%,
  100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-16px);
  }
}

@keyframes blob {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  25% {
    transform: translate(20px, -50px) scale(1.1);
  }
  50% {
    transform: translate(-20px, 20px) scale(0.9);
  }
  75% {
    transform: translate(50px, 50px) scale(1.05);
  }
}

@keyframes blob-delayed {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  25% {
    transform: translate(-30px, 60px) scale(0.8);
  }
  50% {
    transform: translate(30px, -30px) scale(1.1);
  }
  75% {
    transform: translate(-50px, -50px) scale(0.95);
  }
}

@keyframes shine {
  0% {
    left: -100%;
  }
  100% {
    left: 100%;
  }
}

@keyframes slide-down {
  from {
    transform: translateY(-100%);
  }
  to {
    transform: translateY(0);
  }
}

@keyframes slide-right {
  from {
    opacity: 0;
    transform: translateX(-30px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes slide-up {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes scale-in {
  from {
    opacity: 0;
    transform: scale(0.9);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes pulse-custom {
  0%,
  100% {
    transform: scale(1) rotate(0deg);
  }
  50% {
    transform: scale(1.1) rotate(10deg);
  }
}

@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}

.animate-float {
  animation: float 3.5s ease-in-out infinite;
}

.animate-blob {
  animation: blob 8s infinite;
}

.animate-blob-delayed {
  animation: blob-delayed 8s infinite;
}

.animate-shine {
  animation: shine 3.5s infinite;
}

.animate-slide-down {
  animation: slide-down 0.6s ease-out;
}

.animate-slide-right {
  animation: slide-right 0.6s ease-out;
}

.animate-slide-up {
  animation: slide-up 0.6s ease-out;
}

.animate-fade-in {
  animation: fade-in 0.8s ease-out;
}

.animate-scale-in {
  animation: scale-in 0.5s cubic-bezier(0.16, 1, 0.3, 1);
}

.animate-pulse-custom {
  animation: pulse-custom 3s ease-in-out infinite;
}

.animate-shake {
  animation: shake 0.4s ease;
}

.field-error input,
.field-error select {
  border-color: #f43f5e !important;
  box-shadow: 0 0 0 4px rgba(244, 63, 94, 0.15) !important;
  animation: shake 0.4s ease;
}

.group-hover\:scale-115:group-hover {
  transform: scale(1.15);
}

.group-hover\:rotate-10:group-hover {
  transform: rotate(10deg);
}

.group-hover\:rotate-12:group-hover {
  transform: rotate(12deg);
}

.hover\:scale-105:hover {
  transform: scale(1.05);
}
</style>