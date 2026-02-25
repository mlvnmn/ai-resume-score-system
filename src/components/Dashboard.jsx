import React from 'react';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';
import { TrendingUp, Cpu, Award, Zap, AlertCircle, CheckCircle2, Download } from 'lucide-react';
import jsPDF from 'jspdf';

/* ===== PDF REPORT GENERATOR ===== */
const generatePDF = (data) => {
    const doc = new jsPDF('p', 'mm', 'a4');
    const W = doc.internal.pageSize.getWidth();
    const H = doc.internal.pageSize.getHeight();
    const m = 20;
    const cw = W - m * 2;
    let y = 0;

    const checkPage = (need = 14) => {
        if (y + need > H - 25) { doc.addPage(); y = 25; }
    };

    const violet = [124, 58, 237];
    const emerald = [16, 185, 129];
    const amber = [180, 120, 10];
    const red = [200, 50, 60];
    const dark = [30, 30, 40];
    const mid = [100, 100, 115];
    const light = [150, 150, 160];

    // Header band
    doc.setFillColor(...violet);
    doc.rect(0, 0, W, 32, 'F');
    doc.setFont('helvetica', 'bold');
    doc.setFontSize(16);
    doc.setTextColor(255, 255, 255);
    doc.text('ResumeAI', m, 14);
    doc.setFont('helvetica', 'normal');
    doc.setFontSize(9);
    doc.setTextColor(220, 210, 255);
    doc.text('Resume Screening & ATS Analysis Report', m, 21);
    const dateStr = new Date().toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' });
    doc.setFontSize(8);
    doc.text(dateStr, W - m, 14, { align: 'right' });

    y = 42;

    // Resume info
    doc.setFontSize(8);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...mid);
    doc.text('RESUME FILE', m, y);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...dark);
    doc.setFontSize(11);
    doc.text(data.fileName || 'Unknown', m, y + 6);
    y += 16;

    // ATS Score box
    doc.setFillColor(245, 245, 248);
    doc.roundedRect(m, y, cw, 26, 3, 3, 'F');
    doc.setDrawColor(230, 230, 235);
    doc.setLineWidth(0.3);
    doc.roundedRect(m, y, cw, 26, 3, 3, 'S');

    doc.setFontSize(8);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...mid);
    doc.text('ATS COMPATIBILITY SCORE', m + 8, y + 9);

    let scoreColor, scoreLabel;
    if (data.atsScore >= 80) { scoreColor = emerald; scoreLabel = 'Excellent'; }
    else if (data.atsScore >= 60) { scoreColor = violet; scoreLabel = 'Good'; }
    else if (data.atsScore >= 40) { scoreColor = amber; scoreLabel = 'Fair'; }
    else { scoreColor = red; scoreLabel = 'Needs Work'; }

    doc.setFontSize(26);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...scoreColor);
    doc.text(`${data.atsScore}%`, m + 8, y + 21);
    doc.setFontSize(10);
    doc.text(scoreLabel, m + 32, y + 21);

    doc.setFontSize(8);
    doc.setFont('helvetica', 'normal');
    doc.setTextColor(...light);
    doc.text('Industry Avg: 62%', W - m - 8, y + 16, { align: 'right' });

    y += 34;

    // Skill table
    doc.setFontSize(12);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...dark);
    doc.text('Skill Match Breakdown', m, y);
    y += 7;

    doc.setFillColor(235, 235, 240);
    doc.rect(m, y, cw, 7, 'F');
    doc.setFontSize(7);
    doc.setFont('helvetica', 'bold');
    doc.setTextColor(...mid);
    doc.text('SKILL', m + 4, y + 5);
    doc.text('MATCH', m + 70, y + 5);
    doc.text('STATUS', W - m - 4, y + 5, { align: 'right' });
    y += 7;

    data.skills.forEach((skill, i) => {
        checkPage(8);
        if (i % 2 === 0) { doc.setFillColor(250, 250, 252); doc.rect(m, y, cw, 8, 'F'); }

        doc.setFont('helvetica', 'normal');
        doc.setFontSize(9);
        doc.setTextColor(...dark);
        doc.text(skill.name, m + 4, y + 5.5);

        const barX = m + 70;
        const barW = 55;
        doc.setFillColor(230, 230, 235);
        doc.roundedRect(barX, y + 2.5, barW, 3, 1.5, 1.5, 'F');
        if (skill.percentage > 0) {
            const fw = Math.max(2, (skill.percentage / 100) * barW);
            if (skill.percentage >= 70) doc.setFillColor(...emerald);
            else if (skill.percentage >= 40) doc.setFillColor(...violet);
            else doc.setFillColor(245, 158, 11);
            doc.roundedRect(barX, y + 2.5, fw, 3, 1.5, 1.5, 'F');
        }

        const st = skill.percentage >= 70 ? 'Strong' : skill.percentage >= 40 ? 'Partial' : 'Missing';
        const sc = skill.percentage >= 70 ? emerald : skill.percentage >= 40 ? violet : red;
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(7.5);
        doc.setTextColor(...sc);
        doc.text(st, W - m - 4, y + 5.5, { align: 'right' });
        y += 8;
    });

    doc.setDrawColor(230, 230, 235);
    doc.setLineWidth(0.3);
    doc.line(m, y, W - m, y);
    y += 10;

    // Missing keywords
    if (data.missingKeywords && data.missingKeywords.length > 0) {
        checkPage(22);
        doc.setFontSize(12);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(...dark);
        doc.text('Missing Keywords', m, y);
        y += 4;
        doc.setFontSize(7.5);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(...light);
        doc.text('These skills are required but were not found in your resume.', m, y + 3);
        y += 9;

        let px = m;
        doc.setFontSize(8);
        data.missingKeywords.forEach((kw) => {
            const tw = doc.getTextWidth(kw) + 10;
            if (px + tw > W - m) { px = m; y += 9; checkPage(10); }
            doc.setFillColor(254, 243, 199);
            doc.roundedRect(px, y, tw, 6, 2, 2, 'F');
            doc.setFont('helvetica', 'bold');
            doc.setTextColor(146, 100, 12);
            doc.text(kw, px + 5, y + 4.2);
            px += tw + 3;
        });
        y += 14;
    }

    // Recommendations
    if (data.recommendations && data.recommendations.length > 0) {
        checkPage(22);
        doc.setFontSize(12);
        doc.setFont('helvetica', 'bold');
        doc.setTextColor(...dark);
        doc.text('Improvement Recommendations', m, y);
        y += 8;

        data.recommendations.forEach((rec, i) => {
            checkPage(16);
            const lines = doc.splitTextToSize(rec, cw - 14);
            const bh = lines.length * 4.5 + 5;

            doc.setFillColor(...violet);
            doc.circle(m + 4, y + 3, 3, 'F');
            doc.setFont('helvetica', 'bold');
            doc.setFontSize(7);
            doc.setTextColor(255, 255, 255);
            doc.text(`${i + 1}`, m + 4, y + 4, { align: 'center' });

            doc.setFont('helvetica', 'normal');
            doc.setFontSize(8.5);
            doc.setTextColor(...dark);
            lines.forEach((line, li) => { doc.text(line, m + 12, y + 2 + li * 4.5); });

            y += bh + 2;
            if (i < data.recommendations.length - 1) {
                doc.setDrawColor(235, 235, 240);
                doc.setLineWidth(0.2);
                doc.line(m + 12, y, W - m, y);
                y += 4;
            }
        });
    }

    // Footer
    const pages = doc.internal.getNumberOfPages();
    for (let p = 1; p <= pages; p++) {
        doc.setPage(p);
        doc.setDrawColor(...violet);
        doc.setLineWidth(0.5);
        doc.line(m, H - 15, W - m, H - 15);
        doc.setFontSize(7);
        doc.setFont('helvetica', 'normal');
        doc.setTextColor(...light);
        doc.text('Generated by ResumeAI', m, H - 10);
        doc.text(`Page ${p} of ${pages}`, W - m, H - 10, { align: 'right' });
    }

    const safeName = (data.fileName || 'resume').replace(/\.[^.]+$/, '');
    doc.save(`ResumeAI_Report_${safeName}.pdf`);
};


/* ===== ATS SCORE RING ===== */
const AtsScoreCard = ({ score }) => {
    const data = [
        { name: 'Score', value: score },
        { name: 'Remaining', value: 100 - score },
    ];
    const COLORS = ['url(#scoreGradient)', '#1c1c21'];

    let label = 'Needs Work';
    let labelColor = '#ef4444';
    if (score >= 80) { label = 'Excellent'; labelColor = '#10b981'; }
    else if (score >= 60) { label = 'Good'; labelColor = '#a78bfa'; }
    else if (score >= 40) { label = 'Fair'; labelColor = '#f59e0b'; }

    return (
        <div className="card ats-score-card animate-in">
            <div className="card-header">
                <span className="card-title">ATS Compatibility Score</span>
            </div>
            <div className="ats-chart-wrapper">
                <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                        <defs>
                            <linearGradient id="scoreGradient" x1="0" y1="0" x2="1" y2="1">
                                <stop offset="0%" stopColor="#a78bfa" />
                                <stop offset="100%" stopColor="#34d399" />
                            </linearGradient>
                        </defs>
                        <Pie
                            data={data}
                            cx="50%"
                            cy="50%"
                            innerRadius={65}
                            outerRadius={85}
                            paddingAngle={4}
                            dataKey="value"
                            stroke="none"
                            startAngle={90}
                            endAngle={-270}
                        >
                            {data.map((_, index) => (
                                <Cell key={index} fill={COLORS[index]} cornerRadius={10} />
                            ))}
                        </Pie>
                        <text x="50%" y="46%" textAnchor="middle" fill="#ededef" fontSize="32" fontWeight="800" fontFamily="Inter">
                            {score}%
                        </text>
                        <text x="50%" y="60%" textAnchor="middle" fill={labelColor} fontSize="12" fontWeight="600" fontFamily="Inter">
                            {label}
                        </text>
                    </PieChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
};

/* ===== SKILL MATCH BARS ===== */
const SkillMatchCard = ({ skills }) => {
    return (
        <div className="card animate-in">
            <div className="card-header">
                <span className="card-title">Skill Match Analysis</span>
            </div>
            <div className="skill-list">
                {skills.map((skill, i) => (
                    <div key={i}>
                        <div className="skill-item-header">
                            <span className="skill-name">{skill.name}</span>
                            <span className="skill-percent">{skill.percentage}%</span>
                        </div>
                        <div className="skill-bar-track">
                            <div
                                className="skill-bar-fill"
                                style={{ width: `${skill.percentage}%` }}
                            />
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

/* ===== STAT CARD ===== */
const STATS = [
    { icon: Cpu, label: 'AI Match', value: 'High', colorClass: 'blue' },
    { icon: Award, label: 'Experience', value: 'Mid-Senior', colorClass: 'cyan' },
    { icon: Zap, label: 'Readability', value: 'Great', colorClass: 'green' },
    { icon: TrendingUp, label: 'Market Fit', value: 'Strong', colorClass: 'amber' },
];

/* ===== FEEDBACK PANEL ===== */
const FeedbackPanel = ({ keywords, recommendations }) => (
    <div className="feedback-grid">
        <div className="card animate-in">
            <div className="card-header">
                <AlertCircle style={{ width: 16, height: 16, color: 'var(--warning)' }} />
                <span className="card-title" style={{ color: 'var(--warning)' }}>Missing Keywords</span>
            </div>
            <div className="keyword-tags">
                {keywords.map((kw, i) => (
                    <span key={i} className="keyword-tag">{kw}</span>
                ))}
            </div>
        </div>

        <div className="card animate-in">
            <div className="card-header">
                <CheckCircle2 style={{ width: 16, height: 16, color: 'var(--success)' }} />
                <span className="card-title" style={{ color: 'var(--success)' }}>Improvement Tips</span>
            </div>
            <div className="recommendation-list">
                {recommendations.map((rec, i) => (
                    <div key={i} className="recommendation-item">
                        <span className="recommendation-dot" />
                        <span>{rec}</span>
                    </div>
                ))}
            </div>
        </div>
    </div>
);

/* ===== MAIN DASHBOARD VIEW ===== */
const DashboardView = ({ data }) => {
    return (
        <div>
            <div className="dashboard-header animate-in">
                <div>
                    <h1>Analysis Dashboard</h1>
                    <p>AI-powered insights for <strong>{data.fileName || 'your resume'}</strong></p>
                </div>
                <div className="dashboard-header-actions">
                    <button
                        className="btn-download"
                        onClick={() => generatePDF(data)}
                    >
                        <Download style={{ width: 16, height: 16 }} />
                        Download Report
                    </button>
                    <div className="header-badge">
                        <TrendingUp />
                        <div>
                            <div className="header-badge-label">Industry Avg</div>
                            <div className="header-badge-value">62%</div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="dashboard-grid-top">
                <AtsScoreCard score={data.atsScore} />
                <SkillMatchCard skills={data.skills} />
            </div>

            <div className="stats-grid">
                {STATS.map((stat, i) => (
                    <div key={i} className="card stat-card animate-in">
                        <div className={`stat-icon-wrapper ${stat.colorClass}`}>
                            <stat.icon />
                        </div>
                        <div>
                            <div className="stat-label">{stat.label}</div>
                            <div className="stat-value">{stat.value}</div>
                        </div>
                    </div>
                ))}
            </div>

            <FeedbackPanel keywords={data.missingKeywords} recommendations={data.recommendations} />
        </div>
    );
};

export default DashboardView;
