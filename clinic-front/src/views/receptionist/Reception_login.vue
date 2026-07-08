<template>
  <div class="login-bg">
    <div class="login-wrapper">
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>

      <div class="login-card">
        <div class="card-header reception-header">
          <div class="icon-ring">
            <span class="material-icon">🧑‍💼</span>
          </div>
          <h1 class="card-title">Receptionist Portal</h1>
          <p class="card-subtitle">Manage appointments and patient check-ins</p>
        </div>

        <div class="card-body">
          <form @submit.prevent="handleLogin">
            <div class="field-group">
              <label class="field-label">Username</label>
              <div class="input-wrapper">
                <span class="input-icon">👤</span>
                <input
                  v-model="username"
                  type="text"
                  class="input-field"
                  placeholder="Your username"
                  required
                />
              </div>
            </div>

            <div class="field-group">
              <label class="field-label">Password</label>
              <div class="input-wrapper">
                <span class="input-icon">🔒</span>
                <input
                  v-model="password"
                  :type="showPass ? 'text' : 'password'"
                  class="input-field"
                  placeholder="Your password"
                  required
                />
                <button type="button" class="eye-btn" @click="showPass = !showPass">
                  {{ showPass ? '🙈' : '👁️' }}
                </button>
              </div>
            </div>

            <div v-if="errorMsg" class="alert alert-error">⚠️ {{ errorMsg }}</div>
            <div v-if="successMsg" class="alert alert-success">✅ {{ successMsg }}</div>

            <button type="submit" class="submit-btn reception-btn" :disabled="loading">
              <span v-if="loading" class="spinner"></span>
              <span v-else>Sign In as Receptionist →</span>
            </button>
          </form>

          <div class="footer-links">
            <router-link to="/login" class="back-link">← Back to Portal</router-link>
            <router-link to="/request" class="back-link">Book Appointment</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { receptionistLogin } from '@services/api'

const showPass   = ref(false)
const username   = ref('')
const password   = ref('')
const errorMsg   = ref('')
const successMsg = ref('')
const loading    = ref(false)

async function handleLogin() {
  errorMsg.value   = ''
  successMsg.value = ''
  loading.value    = true
  try {
    const res = await receptionistLogin(username.value, password.value)
    successMsg.value = `Welcome, ${res.data.user.first_name || res.data.user.username}!`
    // TODO: redirect to receptionist dashboard
  } catch (err: any) {
    errorMsg.value = err.response?.data?.error || 'Login failed. Please check your credentials.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }

.login-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #052e16, #064e3b, #0a3622);
  display: flex; align-items: center; justify-content: center;
  overflow: hidden; position: relative;
}
.login-wrapper { position: relative; z-index: 1; width: 100%; max-width: 440px; padding: 20px; }
.orb {
  position: fixed; border-radius: 50%;
  filter: blur(80px); opacity: 0.25; pointer-events: none;
}
.orb-1 {
  width: 420px; height: 420px; background: #10b981;
  top: -120px; left: -120px; animation: float 8s ease-in-out infinite;
}
.orb-2 {
  width: 320px; height: 320px; background: #0d9488;
  bottom: -100px; right: -100px; animation: float 10s ease-in-out infinite reverse;
}
@keyframes float {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(30px, 30px); }
}

.login-card {
  background: rgba(255,255,255,0.06); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.12); border-radius: 24px;
  box-shadow: 0 32px 64px rgba(0,0,0,0.5); overflow: hidden; animation: slideUp 0.5s ease;
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}

.card-header {
  padding: 40px 40px 28px; text-align: center;
  background: linear-gradient(135deg, rgba(16,185,129,0.25), rgba(13,148,136,0.2));
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.icon-ring {
  width: 72px; height: 72px; border-radius: 50%;
  background: linear-gradient(135deg, #10b981, #0d9488);
  display: flex; align-items: center; justify-content: center;
  margin: 0 auto 16px; box-shadow: 0 8px 24px rgba(16,185,129,0.4); font-size: 32px;
}
.card-title { font-size: 24px; font-weight: 700; color: #fff; letter-spacing: -0.5px; margin-bottom: 6px; }
.card-subtitle { font-size: 14px; color: rgba(255,255,255,0.55); font-weight: 400; }

.card-body { padding: 32px 40px 40px; }
.field-group { margin-bottom: 20px; }
.field-label {
  display: block; font-size: 13px; font-weight: 500;
  color: rgba(255,255,255,0.65); margin-bottom: 8px;
  letter-spacing: 0.5px; text-transform: uppercase;
}
.input-wrapper { position: relative; display: flex; align-items: center; }
.input-icon { position: absolute; left: 14px; font-size: 16px; pointer-events: none; }
.input-field {
  width: 100%; padding: 14px 14px 14px 44px;
  background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px; color: #fff; font-size: 15px; outline: none; transition: all 0.3s;
}
.input-field::placeholder { color: rgba(255,255,255,0.3); }
.input-field:focus {
  border-color: #10b981; background: rgba(16,185,129,0.1);
  box-shadow: 0 0 0 3px rgba(16,185,129,0.15);
}
.eye-btn {
  position: absolute; right: 12px; background: none; border: none;
  cursor: pointer; font-size: 16px; padding: 4px; border-radius: 6px; transition: transform 0.2s;
}
.eye-btn:hover { transform: scale(1.15); }

.alert { padding: 12px 16px; border-radius: 10px; font-size: 13px; margin-bottom: 16px; font-weight: 500; }
.alert-error { background: rgba(239,68,68,0.15); border: 1px solid rgba(239,68,68,0.3); color: #fca5a5; }
.alert-success { background: rgba(34,197,94,0.15); border: 1px solid rgba(34,197,94,0.3); color: #86efac; }

.submit-btn {
  width: 100%; padding: 15px; border: none; border-radius: 12px;
  font-size: 15px; font-weight: 600; cursor: pointer; transition: all 0.3s;
  display: flex; align-items: center; justify-content: center;
  gap: 8px; margin-bottom: 24px; letter-spacing: 0.3px;
}
.reception-btn {
  background: linear-gradient(135deg, #10b981, #0d9488);
  color: #fff; box-shadow: 0 8px 24px rgba(16,185,129,0.4);
}
.reception-btn:hover:not(:disabled) { transform: translateY(-2px); box-shadow: 0 12px 32px rgba(16,185,129,0.5); }
.reception-btn:disabled { opacity: 0.6; cursor: not-allowed; }

.spinner {
  width: 18px; height: 18px; border: 2px solid rgba(255,255,255,0.3);
  border-top-color: #fff; border-radius: 50%; animation: spin 0.8s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

.footer-links { display: flex; justify-content: space-between; align-items: center; }
.back-link {
  color: rgba(255,255,255,0.45); text-decoration: none;
  font-size: 13px; font-weight: 500; transition: color 0.2s;
}
.back-link:hover { color: #10b981; }
</style>
