<template>
  <div class="portal-bg">
    <div class="portal-wrapper">
      <div class="orb orb-1"></div>
      <div class="orb orb-2"></div>
      <div class="orb orb-3"></div>

      <div class="portal-card">
        <!-- Brand Header -->
        <div class="portal-header">
          <div class="brand-logo">🏥</div>
          <h1 class="brand-name">ClinicCare</h1>
          <p class="brand-tagline">Your trusted healthcare management portal</p>
        </div>

        <!-- Role Selection -->
        <div class="portal-body">
          <p class="section-label">Select your role to continue</p>

          <div class="role-cards">
            <router-link to="/doctor/login" class="role-card doctor-card">
              <div class="role-icon">🩺</div>
              <div class="role-info">
                <span class="role-title">Doctor</span>
                <span class="role-desc">View patients & appointments</span>
              </div>
              <span class="role-arrow">→</span>
            </router-link>

            <router-link to="/admin/login" class="role-card admin-card">
              <div class="role-icon">🛡️</div>
              <div class="role-info">
                <span class="role-title">Administrator</span>
                <span class="role-desc">Manage clinic operations</span>
              </div>
              <span class="role-arrow">→</span>
            </router-link>

            <router-link to="/receptionist/login" class="role-card reception-card">
              <div class="role-icon">🧑‍💼</div>
              <div class="role-info">
                <span class="role-title">Receptionist</span>
                <span class="role-desc">Handle check-ins & scheduling</span>
              </div>
              <span class="role-arrow">→</span>
            </router-link>
          </div>

          <div class="divider">
            <span class="divider-line"></span>
            <span class="divider-text">or</span>
            <span class="divider-line"></span>
          </div>

          <router-link to="/request" class="patient-btn">
            📅 Book an Appointment as Patient
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
// Navigation handled by router-link / to="" attributes
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }

.portal-bg {
  min-height: 100vh;
  background: linear-gradient(135deg, #0f0c29, #24243e, #302b63);
  display: flex; align-items: center; justify-content: center;
  overflow: hidden; position: relative;
}
.portal-wrapper { position: relative; z-index: 1; width: 100%; max-width: 480px; padding: 20px; }

.orb {
  position: fixed; border-radius: 50%;
  filter: blur(90px); opacity: 0.2; pointer-events: none;
}
.orb-1 { width: 500px; height: 500px; background: #3b82f6; top: -150px; left: -150px; animation: float 9s ease-in-out infinite; }
.orb-2 { width: 380px; height: 380px; background: #c026d3; bottom: -100px; right: -100px; animation: float 11s ease-in-out infinite reverse; }
.orb-3 { width: 250px; height: 250px; background: #10b981; top: 50%; left: 50%; animation: float 7s ease-in-out infinite 2s; }
@keyframes float {
  0%, 100% { transform: translate(0, 0); }
  50% { transform: translate(25px, 25px); }
}

.portal-card {
  background: rgba(255,255,255,0.06); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px);
  border: 1px solid rgba(255,255,255,0.12); border-radius: 28px;
  box-shadow: 0 40px 80px rgba(0,0,0,0.5); overflow: hidden;
  animation: slideUp 0.6s cubic-bezier(0.22, 1, 0.36, 1);
}
@keyframes slideUp {
  from { opacity: 0; transform: translateY(40px) scale(0.97); }
  to   { opacity: 1; transform: translateY(0) scale(1); }
}

.portal-header {
  padding: 48px 40px 32px; text-align: center;
  background: linear-gradient(135deg, rgba(59,130,246,0.15), rgba(192,38,211,0.1), rgba(16,185,129,0.1));
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.brand-logo { font-size: 56px; display: block; margin-bottom: 12px; animation: pulse 3s ease-in-out infinite; }
@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.06); }
}
.brand-name { font-size: 30px; font-weight: 800; color: #fff; letter-spacing: -1px; margin-bottom: 6px; }
.brand-tagline { font-size: 14px; color: rgba(255,255,255,0.5); font-weight: 400; }

.portal-body { padding: 32px 40px 40px; }
.section-label {
  font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 1.2px; color: rgba(255,255,255,0.4);
  text-align: center; margin-bottom: 20px;
}

.role-cards { display: flex; flex-direction: column; gap: 12px; margin-bottom: 28px; }
.role-card {
  display: flex; align-items: center; gap: 14px;
  padding: 16px 20px; border-radius: 16px;
  border: 1px solid rgba(255,255,255,0.08);
  text-decoration: none; transition: all 0.3s;
  position: relative; overflow: hidden;
}
.role-card::before {
  content: ''; position: absolute; inset: 0; opacity: 0;
  transition: opacity 0.3s;
}
.role-card:hover::before { opacity: 1; }
.role-card:hover { transform: translateX(4px); border-color: rgba(255,255,255,0.2); }

.doctor-card { background: rgba(59,130,246,0.1); }
.doctor-card::before { background: rgba(59,130,246,0.1); }
.doctor-card:hover { box-shadow: 0 8px 24px rgba(59,130,246,0.2); }

.admin-card { background: rgba(192,38,211,0.1); }
.admin-card::before { background: rgba(192,38,211,0.1); }
.admin-card:hover { box-shadow: 0 8px 24px rgba(192,38,211,0.2); }

.reception-card { background: rgba(16,185,129,0.1); }
.reception-card::before { background: rgba(16,185,129,0.1); }
.reception-card:hover { box-shadow: 0 8px 24px rgba(16,185,129,0.2); }

.role-icon { font-size: 28px; flex-shrink: 0; }
.role-info { flex: 1; }
.role-title { display: block; font-size: 15px; font-weight: 600; color: #fff; margin-bottom: 2px; }
.role-desc { display: block; font-size: 12px; color: rgba(255,255,255,0.45); }
.role-arrow { font-size: 18px; color: rgba(255,255,255,0.35); transition: transform 0.3s; }
.role-card:hover .role-arrow { transform: translateX(4px); color: rgba(255,255,255,0.7); }

.divider {
  display: flex; align-items: center; gap: 12px; margin-bottom: 20px;
}
.divider-line { flex: 1; height: 1px; background: rgba(255,255,255,0.1); }
.divider-text { font-size: 12px; color: rgba(255,255,255,0.3); font-weight: 500; }

.patient-btn {
  display: block; width: 100%; padding: 15px; border-radius: 14px;
  background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12);
  color: rgba(255,255,255,0.8); text-decoration: none; text-align: center;
  font-size: 14px; font-weight: 600; letter-spacing: 0.2px; transition: all 0.3s;
}
.patient-btn:hover {
  background: rgba(255,255,255,0.12); color: #fff;
  border-color: rgba(255,255,255,0.25); transform: translateY(-1px);
}
</style>
