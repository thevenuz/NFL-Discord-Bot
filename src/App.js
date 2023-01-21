import {Route, Routes} from 'react-router-dom';
import PrivacyPolicy from './components/PrivacyPolicy';
import TermsOfService from './components/TermsOfService';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App bg-gray-800 flex flex-col min-h-screen font-Source-Sans text-slate-50">
        <Header />
        <Routes>
          <Route path="/" element={<PrivacyPolicy />} />
          <Route path="privacy-policy" element={<PrivacyPolicy />} />
          <Route path="terms-of-service" element={<TermsOfService />} />
        </Routes>
        <Footer />
    </div>
  );
}

export default App;
