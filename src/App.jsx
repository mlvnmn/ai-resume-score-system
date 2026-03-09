import React, { useState } from 'react';
import './index.css';
import Sidebar from './components/Sidebar';
import ResumeUpload from './components/ResumeUpload';
import DashboardView from './components/Dashboard';
import BatchUpload from './components/BatchUpload';
import RankingDashboard from './components/RankingDashboard';
import { FileUp, Users } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('upload');
  const [analysisData, setAnalysisData] = useState(null);
  const [batchData, setBatchData] = useState(null);

  const handleUploadSuccess = (data) => {
    setAnalysisData(data);
    setActiveTab('dashboard');
  };

  const handleBatchUploadSuccess = (data) => {
    setBatchData(data);
    setActiveTab('ranking');
  };

  return (
    <div className="app-container">
      <Sidebar activeTab={activeTab} setActiveTab={setActiveTab} />

      <main className="main-content">
        {activeTab === 'upload' && (
          <ResumeUpload onUploadSuccess={handleUploadSuccess} />
        )}

        {activeTab === 'dashboard' && (
          analysisData ? (
            <DashboardView data={analysisData} />
          ) : (
            <div className="empty-state">
              <div className="card empty-state-card">
                <h2>No Resume Analyzed Yet</h2>
                <p>Upload a resume to get your ATS compatibility score, skill match breakdown, and improvement tips.</p>
                <button className="btn-primary" onClick={() => setActiveTab('upload')}>
                  <FileUp style={{ width: 18, height: 18 }} />
                  Upload Resume
                </button>
              </div>
            </div>
          )
        )}

        {activeTab === 'batch' && (
          <BatchUpload onBatchUploadSuccess={handleBatchUploadSuccess} />
        )}

        {activeTab === 'ranking' && (
          batchData ? (
            <RankingDashboard batchData={batchData} />
          ) : (
            <div className="empty-state">
              <div className="card empty-state-card">
                <h2>No Batch Analysis Yet</h2>
                <p>Upload multiple resumes to see their rankings for a specific role.</p>
                <button className="btn-primary" onClick={() => setActiveTab('batch')}>
                  <Users style={{ width: 18, height: 18 }} />
                  Batch Upload
                </button>
              </div>
            </div>
          )
        )}
      </main>
    </div>
  );
}

export default App;
