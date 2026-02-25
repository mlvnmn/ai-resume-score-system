import React, { useCallback, useState, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import { FileUp, FileText, CheckCircle, FileType, File, Search, X, ChevronDown } from 'lucide-react';

const API_URL = import.meta.env.DEV ? 'http://localhost:8000' : '';

const RoleSearchDropdown = ({ roles, selectedRole, onSelect }) => {
    const [isOpen, setIsOpen] = useState(false);
    const [search, setSearch] = useState('');
    const dropdownRef = React.useRef(null);

    // Close on outside click
    useEffect(() => {
        const handler = (e) => {
            if (dropdownRef.current && !dropdownRef.current.contains(e.target)) {
                setIsOpen(false);
            }
        };
        document.addEventListener('mousedown', handler);
        return () => document.removeEventListener('mousedown', handler);
    }, []);

    const filtered = roles.filter(r =>
        r.title.toLowerCase().includes(search.toLowerCase()) ||
        r.category.toLowerCase().includes(search.toLowerCase())
    );

    // Group by category
    const grouped = filtered.reduce((acc, role) => {
        const cat = role.category || 'Other';
        if (!acc[cat]) acc[cat] = [];
        acc[cat].push(role);
        return acc;
    }, {});

    const selectedTitle = roles.find(r => r.key === selectedRole)?.title || 'Select a role…';

    return (
        <div className="role-search-dropdown" ref={dropdownRef}>
            {/* Trigger button */}
            <button
                type="button"
                className="role-search-trigger"
                onClick={() => { setIsOpen(!isOpen); setSearch(''); }}
            >
                <span className="role-search-trigger-text">{selectedTitle}</span>
                <ChevronDown className={`role-search-chevron ${isOpen ? 'open' : ''}`} />
            </button>

            {/* Dropdown panel */}
            {isOpen && (
                <div className="role-search-panel">
                    {/* Search input */}
                    <div className="role-search-input-wrapper">
                        <Search className="role-search-icon" />
                        <input
                            className="role-search-input"
                            type="text"
                            placeholder="Search roles…"
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            autoFocus
                        />
                        {search && (
                            <button className="role-search-clear" onClick={() => setSearch('')}>
                                <X />
                            </button>
                        )}
                    </div>

                    {/* Results */}
                    <div className="role-search-results">
                        {Object.keys(grouped).length === 0 && (
                            <div className="role-search-empty">No roles found</div>
                        )}
                        {Object.entries(grouped).map(([category, items]) => (
                            <div key={category} className="role-search-group">
                                <div className="role-search-category">{category}</div>
                                {items.map(role => (
                                    <button
                                        key={role.key}
                                        className={`role-search-option ${role.key === selectedRole ? 'active' : ''}`}
                                        onClick={() => {
                                            onSelect(role.key);
                                            setIsOpen(false);
                                            setSearch('');
                                        }}
                                    >
                                        {role.title}
                                        {role.key === selectedRole && <span className="role-check">✓</span>}
                                    </button>
                                ))}
                            </div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

const ResumeUpload = ({ onUploadSuccess }) => {
    const [isUploading, setIsUploading] = useState(false);
    const [uploadedFile, setUploadedFile] = useState(null);
    const [roles, setRoles] = useState([]);
    const [selectedRole, setSelectedRole] = useState('software_engineer');
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`${API_URL}/api/roles`)
            .then(res => res.json())
            .then(data => {
                setRoles(data);
                if (data.length > 0) setSelectedRole(data[0].key);
            })
            .catch(() => {
                setRoles([
                    { key: 'software_engineer', title: 'Software Engineer', category: 'Engineering' },
                    { key: 'data_scientist', title: 'Data Scientist', category: 'Data & Analytics' },
                    { key: 'frontend_developer', title: 'Frontend Developer', category: 'Engineering' },
                    { key: 'devops_engineer', title: 'DevOps Engineer', category: 'DevOps & Cloud' },
                    { key: 'fullstack_developer', title: 'Full Stack Developer', category: 'Engineering' },
                ]);
            });
    }, []);

    const onDrop = useCallback(async (acceptedFiles) => {
        const file = acceptedFiles[0];
        if (!file) return;

        setUploadedFile(file);
        setIsUploading(true);
        setError(null);

        try {
            const formData = new FormData();
            formData.append('file', file);
            formData.append('role', selectedRole);

            const response = await fetch(`${API_URL}/api/analyze`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Analysis failed');
            }

            const data = await response.json();
            setIsUploading(false);

            setTimeout(() => {
                onUploadSuccess(data);
            }, 600);
        } catch (err) {
            setIsUploading(false);
            setError(err.message || 'Failed to connect to the backend. Is the server running?');
            setUploadedFile(null);
        }
    }, [onUploadSuccess, selectedRole]);

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            'application/pdf': ['.pdf'],
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
            'application/msword': ['.doc'],
        },
        multiple: false,
    });

    const renderContent = () => {
        if (isUploading) {
            return (
                <div className="upload-analyzing">
                    <div className="spinner" />
                    <div className="upload-analyzing-title">Analyzing your resume…</div>
                    <div className="upload-analyzing-desc">
                        Extracting skills, computing ATS score, and generating recommendations.
                    </div>
                </div>
            );
        }

        if (uploadedFile && !isUploading && !error) {
            return (
                <div className="upload-success">
                    <div className="upload-success-icon">
                        <CheckCircle />
                    </div>
                    <div className="upload-success-file">{uploadedFile.name}</div>
                    <div className="upload-success-msg">
                        <CheckCircle style={{ width: 16, height: 16 }} />
                        Analysis complete — loading results…
                    </div>
                </div>
            );
        }

        return (
            <>
                <div className="dropzone-icon">
                    <FileUp />
                </div>
                <div className="dropzone-text">Drag & drop your resume here</div>
                <div className="dropzone-hint">Supports PDF, DOCX, and DOC — max 5 MB</div>
                <button type="button" className="dropzone-btn">Browse Files</button>
            </>
        );
    };

    return (
        <div className="upload-view">
            <div className="upload-header">
                <h1 className="upload-title">Optimize Your Resume</h1>
                <p className="upload-subtitle">
                    Upload your resume and let our AI analyze it against real job descriptions.
                </p>
            </div>

            {/* Searchable Role Selector */}
            <div className="role-selector">
                <label className="role-label">Target Role</label>
                <RoleSearchDropdown
                    roles={roles}
                    selectedRole={selectedRole}
                    onSelect={setSelectedRole}
                />
            </div>

            <div
                {...getRootProps()}
                className={`dropzone ${isDragActive ? 'drag-active' : ''}`}
            >
                <input {...getInputProps()} />
                {renderContent()}
            </div>

            {error && (
                <div className="upload-error">
                    <span>⚠ {error}</span>
                </div>
            )}

            <div className="upload-formats">
                <div className="format-badge">
                    <FileText />
                    <span>PDF format</span>
                </div>
                <div className="format-badge">
                    <FileType />
                    <span>DOCX format</span>
                </div>
                <div className="format-badge">
                    <File />
                    <span>DOC format</span>
                </div>
            </div>
        </div>
    );
};

export default ResumeUpload;
