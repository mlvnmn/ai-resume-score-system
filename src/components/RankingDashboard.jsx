import React, { useState } from 'react';
import { Trophy, Star, AlertCircle, ArrowLeft, Eye } from 'lucide-react';
import DashboardView from './Dashboard';

const RankingDashboard = ({ batchData }) => {
    const [selectedCandidate, setSelectedCandidate] = useState(null);

    const { results = [], failed = [] } = batchData;

    if (selectedCandidate) {
        return (
            <div className="ranking-detail-view">
                <button 
                    className="btn-back" 
                    onClick={() => setSelectedCandidate(null)}
                >
                    <ArrowLeft size={18} />
                    Back to Rankings
                </button>
                <div style={{ marginTop: '1.5rem' }}>
                    <DashboardView data={selectedCandidate} />
                </div>
                <style>{`
                .btn-back {
                    display: inline-flex;
                    align-items: center;
                    gap: 0.5rem;
                    padding: 0.6rem 1.15rem;
                    background: var(--bg-card);
                    border: 1px solid var(--border-color);
                    border-radius: var(--radius-md);
                    color: var(--text-primary);
                    font-size: 0.82rem;
                    font-weight: 600;
                    cursor: pointer;
                    transition: var(--transition);
                }
                .btn-back:hover {
                    border-color: var(--accent-blue);
                    color: var(--accent-blue);
                }
                `}</style>
            </div>
        );
    }

    return (
        <div className="ranking-dashboard">
            <div className="dashboard-header">
                <div>
                    <h1>Candidate Rankings</h1>
                    <p>Analyzed {results.length} resumes successfully. Ranked by ATS compatibility.</p>
                </div>
                <div className="header-badge">
                    <Trophy style={{ color: "var(--warning)" }} />
                    <div className="header-badge-content">
                        <div className="header-badge-label">Top Score</div>
                        <div className="header-badge-value">
                            {results.length > 0 ? `${results[0].atsScore}%` : 'N/A'}
                        </div>
                    </div>
                </div>
            </div>

            {results.length > 0 ? (
                <div className="ranking-list">
                    <div className="ranking-grid-header">
                        <div className="col-rank">Rank</div>
                        <div className="col-name">Candidate Resume</div>
                        <div className="col-score">ATS Score</div>
                        <div className="col-actions">Actions</div>
                    </div>
                    {results.map((candidate, idx) => (
                        <div key={idx} className={`ranking-row ${idx === 0 ? 'top-rank' : ''}`}>
                            <div className="col-rank">
                                {idx === 0 ? (
                                    <div className="rank-badge gold"><Trophy size={16} /> 1</div>
                                ) : idx === 1 ? (
                                    <div className="rank-badge silver">2</div>
                                ) : idx === 2 ? (
                                    <div className="rank-badge bronze">3</div>
                                ) : (
                                    <div className="rank-number">{idx + 1}</div>
                                )}
                            </div>
                            <div className="col-name">
                                <div className="candidate-name">{candidate.fileName}</div>
                                <div className="candidate-skills-preview">
                                    {candidate.skills.slice(0, 3).map(s => s.name).join(', ')}
                                    {candidate.skills.length > 3 && '...'}
                                </div>
                            </div>
                            <div className="col-score">
                                <div className="score-badge">
                                    <Star size={14} className={candidate.atsScore >= 75 ? 'star-good' : 'star-avg'} />
                                    <span>{candidate.atsScore}%</span>
                                </div>
                            </div>
                            <div className="col-actions">
                                <button className="btn-view" onClick={() => setSelectedCandidate(candidate)}>
                                    <Eye size={16} /> View Details
                                </button>
                            </div>
                        </div>
                    ))}
                </div>
            ) : (
                <div className="card" style={{ padding: '2rem', textAlign: 'center' }}>
                    <p>No candidates processed successfully.</p>
                </div>
            )}

            {failed.length > 0 && (
                <div className="failed-files card">
                    <h3 style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--danger)', marginBottom: '1rem' }}>
                        <AlertCircle size={18} /> Failed to Process ({failed.length})
                    </h3>
                    <ul className="failed-list">
                        {failed.map((err, i) => (
                            <li key={i}>{err}</li>
                        ))}
                    </ul>
                </div>
            )}

            <style>{`
            .ranking-dashboard {
                animation: fadeIn 0.4s ease-out;
            }
            .ranking-list {
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-lg);
                overflow: hidden;
                margin-bottom: 2rem;
            }
            .ranking-grid-header {
                display: flex;
                padding: 1rem 1.5rem;
                background: rgba(255, 255, 255, 0.02);
                border-bottom: 1px solid var(--border-color);
                font-size: 0.75rem;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: var(--text-muted);
            }
            .ranking-row {
                display: flex;
                align-items: center;
                padding: 1.25rem 1.5rem;
                border-bottom: 1px solid rgba(255, 255, 255, 0.04);
                transition: var(--transition);
            }
            .ranking-row:last-child {
                border-bottom: none;
            }
            .ranking-row:hover {
                background: rgba(255, 255, 255, 0.02);
            }
            .ranking-row.top-rank {
                background: linear-gradient(90deg, rgba(251, 191, 36, 0.08), transparent);
                border-left: 3px solid var(--warning);
            }
            .col-rank { width: 80px; flex-shrink: 0; }
            .col-name { flex: 1; min-width: 0; }
            .col-score { width: 120px; flex-shrink: 0; }
            .col-actions { width: 140px; flex-shrink: 0; display: flex; justify-content: flex-end; }

            .rank-badge {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                gap: 0.25rem;
                width: 44px;
                height: 28px;
                border-radius: var(--radius-sm);
                font-weight: 700;
                font-size: 0.85rem;
            }
            .rank-badge.gold { background: rgba(251, 191, 36, 0.2); color: #fcd34d; width: 60px; }
            .rank-badge.silver { background: rgba(156, 163, 175, 0.2); color: #d1d5db; }
            .rank-badge.bronze { background: rgba(180, 83, 9, 0.2); color: #fcb69f; }
            .rank-number { font-weight: 600; color: var(--text-secondary); padding-left: 0.75rem; }

            .candidate-name { font-weight: 600; color: var(--text-primary); margin-bottom: 0.25rem; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            .candidate-skills-preview { font-size: 0.8rem; color: var(--text-muted); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }

            .score-badge { display: flex; align-items: center; gap: 0.35rem; font-weight: 700; font-size: 1.1rem; }
            .star-good { color: var(--success); }
            .star-avg { color: var(--warning); }

            .btn-view {
                display: flex;
                align-items: center;
                gap: 0.4rem;
                padding: 0.5rem 0.85rem;
                background: transparent;
                border: 1px solid var(--border-color);
                border-radius: var(--radius-sm);
                color: var(--text-primary);
                font-size: 0.8rem;
                font-weight: 500;
                transition: var(--transition);
            }
            .btn-view:hover {
                border-color: var(--accent-blue);
                color: var(--accent-blue);
                background: rgba(167, 139, 250, 0.05);
            }

            .failed-list { margin-left: 1.5rem; font-size: 0.85rem; color: var(--text-secondary); }
            .failed-list li { margin-bottom: 0.25rem; }
            `}</style>
        </div>
    );
};

export default RankingDashboard;
