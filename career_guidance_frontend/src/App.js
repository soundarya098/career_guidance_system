import React, { useState } from "react";
import "./App.css";

function App() {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    age: 21,
    math: 3,
    programming: 3,
    creativity: 3,
    communication: 3,
    logic: 3,
    preferred_subject: "Computer Science"
  });
  const [prediction, setPrediction] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const nextStep = () => setStep(step + 1);
  const prevStep = () => setStep(step - 1);

  const handleSubmit = async () => {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    setPrediction(data.prediction);
    setStep(4);
  };

  return (
    <div className="container">
      <h1 className="title">🎯 AI-Based Career Guidance System</h1>

      {step === 1 && (
        <div className="card">
          <h2>Step 1: Personal Info</h2>
          <label>Age: {formData.age}</label>
          <input type="range" min="18" max="40" name="age" value={formData.age} onChange={handleChange} />
          <button onClick={nextStep}>Next ➡️</button>
        </div>
      )}

      {step === 2 && (
        <div className="card">
          <h2>Step 2: Skill Ratings (1–5)</h2>
          {["math", "programming", "creativity", "communication", "logic"].map((skill) => (
            <div key={skill}>
              <label>{skill.charAt(0).toUpperCase() + skill.slice(1)}: {formData[skill]}</label>
              <input type="range" min="1" max="5" name={skill} value={formData[skill]} onChange={handleChange} />
            </div>
          ))}
          <div className="buttons">
            <button onClick={prevStep}>⬅️ Back</button>
            <button onClick={nextStep}>Next ➡️</button>
          </div>
        </div>
      )}

      {step === 3 && (
        <div className="card">
          <h2>Step 3: Choose Your Favorite Subject</h2>
          <select name="preferred_subject" value={formData.preferred_subject} onChange={handleChange}>
            <option>Physics</option>
            <option>Maths</option>
            <option>Computer Science</option>
            <option>Biology</option>
            <option>Chemistry</option>
            <option>Economics</option>
          </select>
          <div className="buttons">
            <button onClick={prevStep}>⬅️ Back</button>
            <button onClick={handleSubmit}>🔍 Predict Career</button>
          </div>
        </div>
      )}

      {step === 4 && (
        <div className="card result">
          <h2>🎓 Your Recommended Career:</h2>
          <h3 className="prediction">{prediction}</h3>
          <button onClick={() => setStep(1)}>Start Again 🔁</button>
        </div>
      )}

      <footer>Developed by <b>Soundarya G M 💻</b></footer>
    </div>
  );
}

export default App;
