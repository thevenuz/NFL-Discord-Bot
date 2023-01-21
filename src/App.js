import {Route, Routes} from 'react-router-dom';
import PrivacyPolicy from './components/PrivacyPolicy';
import TermsOfService from './components/TermsOfService';
import Header from './components/Header';
import Footer from './components/Footer';

function App() {
  return (
    <div className="App bg-gray-800 flex flex-col min-h-screen font-Source-Sans text-slate-50">
      {/* <div className='flex'> */}
        <Header />
      {/* </div>
      <div className='flex-1 flex-col h-auto'> */}
        <Routes>
          <Route path="/" element={<PrivacyPolicy />} />
          <Route path="privacy-policy" element={<PrivacyPolicy />} />
          <Route path="terms-of-service" element={<TermsOfService />} />
        </Routes>
      {/* </div>
      <div className='flex'> */}
        <Footer />
      {/* </div> */}
    </div>
  );
}

export default App;
