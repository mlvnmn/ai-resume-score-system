import React from 'react';
import { LayoutDashboard, FileUp, Scan, Users } from 'lucide-react';

const Sidebar = ({ activeTab, setActiveTab }) => {
  const mainNav = [
    { id: 'dashboard', icon: LayoutDashboard, label: 'Dashboard' },
    { id: 'upload', icon: FileUp, label: 'Upload Resume' },
    { id: 'batch', icon: Users, label: 'Batch Rank' },
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="sidebar-brand-icon">
          <Scan />
        </div>
        <span className="sidebar-brand-text">ResumeAI</span>
      </div>

      <nav className="sidebar-nav">
        <span className="sidebar-section-label">Main Menu</span>
        {mainNav.map((item) => (
          <button
            key={item.id}
            onClick={() => setActiveTab(item.id)}
            className={`sidebar-item ${activeTab === item.id ? 'active' : ''}`}
          >
            <item.icon />
            <span>{item.label}</span>
          </button>
        ))}
      </nav>
    </aside>
  );
};

export default Sidebar;

