/**
 * router/index.ts
 *
 * Routes for the Clinic Appointment app
 */

import { createRouter, createWebHistory } from 'vue-router'

// Views
import RequestView        from '../views/patients/Request.vue'
import DoctorLoginView    from '../views/doctor/Doctor_login.vue'
import AdminLoginView     from '../views/admin/Admin_login.vue'
import ReceptionLoginView from '../views/receptionist/Reception_login.vue'
import AuthLoginView      from '../views/auth/login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // Default → patient request page
    {
      path: '/',
      redirect: '/request',
    },
    {
      path: '/request',
      name: 'request',
      component: RequestView,
    },
    // Staff portal
    {
      path: '/login',
      name: 'login',
      component: AuthLoginView,
    },
    {
      path: '/doctor/login',
      name: 'doctor-login',
      component: DoctorLoginView,
    },
    {
      path: '/admin/login',
      name: 'admin-login',
      component: AdminLoginView,
    },
    {
      path: '/receptionist/login',
      name: 'receptionist-login',
      component: ReceptionLoginView,
    },
    // Redirect aliases to support request/doctor_login etc.
    {
      path: '/request/doctor_login',
      redirect: '/doctor/login',
    },
    {
      path: '/request/doctor-login',
      redirect: '/doctor/login',
    },
    {
      path: '/request/admin_login',
      redirect: '/admin/login',
    },
    {
      path: '/request/admin-login',
      redirect: '/admin/login',
    },
    {
      path: '/request/reception_login',
      redirect: '/receptionist/login',
    },
    {
      path: '/request/reception-login',
      redirect: '/receptionist/login',
    },
    {
      path: '/request/receptionist_login',
      redirect: '/receptionist/login',
    },
    {
      path: '/request/receptionist-login',
      redirect: '/receptionist/login',
    },
  ],
})

export default router
