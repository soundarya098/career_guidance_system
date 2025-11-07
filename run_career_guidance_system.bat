@echo off
echo =====================================
echo   Starting AI Career Guidance System
echo =====================================

REM --- Navigate to backend folder ---
cd /d "C:\Users\user\Downloads\career_guidance_system\career_guidance_backend"
echo Starting backend server...
start cmd /k "python app.py"

REM Wait 5 seconds for backend to start
timeout /t 5 /nobreak >nul

REM --- Navigate to frontend folder ---
cd /d "C:\Users\user\Downloads\career_guidance_system\career_guidance_frontend"
echo Starting frontend (React app)...
start cmd /k "npm start"

REM Wait a few seconds then open browser automatically
timeout /t 10 /nobreak >nul
start "" "http://localhost:3000"

echo =====================================
echo  Both servers started successfully!
echo  Your app should open in the browser.
echo =====================================
pause
