import { Routes, Route } from 'react-router'
import Home from './pages/Home'
import IELTSCalculator from './pages/IELTSCalculator'
import OETSpeaking from './pages/OETSpeaking'
import OSCEPractice from './pages/OSCEPractice'
import AIPromptGenerator from './pages/AIPromptGenerator'
import LanguageGuide from './pages/LanguageGuide'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/ielts-calculator" element={<IELTSCalculator />} />
      <Route path="/oet-speaking" element={<OETSpeaking />} />
      <Route path="/osce-practice" element={<OSCEPractice />} />
      <Route path="/ai-prompt-generator" element={<AIPromptGenerator />} />
      <Route path="/language-guide" element={<LanguageGuide />} />
    </Routes>
  )
}
