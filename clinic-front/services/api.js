import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
})

// Authentication services
export const doctorLogin = (username, password) => {
  return api.post('/doctor/login/', { username, password })
}

export const adminLogin = (username, password) => {
  return api.post('/admin/login/', { username, password })
}

export const receptionistLogin = (username, password) => {
  return api.post('/receptionist/login/', { username, password })
}

// Doctors
export const getDoctors = () => {
  return api.get('/doctors/')
}

// Appointments
export const requestAppointment = (payload) => {
  return api.post('/appointment/request/', payload)
}

export default api
