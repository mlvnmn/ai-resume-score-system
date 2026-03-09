import React, { useCallback, useState, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';
import { FileUp, FileText, CheckCircle, FileType, File, Search, X, ChevronDown, Users } from 'lucide-react';

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

    const selectedTitle = roles.find(r => r.key === selectedRole)?.title || 'Select a role...';

    return (
        <div className="role-search-dropdown" ref={dropdownRef}>
            <button
                type="button"
                className="role-search-trigger"
                onClick={() => { setIsOpen(!isOpen); setSearch(''); }}
            >
                <span className="role-search-trigger-text">{selectedTitle}</span>
                <ChevronDown className={`role-search-chevron ${isOpen ? 'open' : ''}`} />
            </button>

            {isOpen && (
                <div className="role-search-panel">
                    <div className="role-search-input-wrapper">
                        <Search className="role-search-icon" />
                        <input
                            className="role-search-input"
                            type="text"
                            placeholder="Search roles..."
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

const BatchUpload = ({ onBatchUploadSuccess }) => {
    const [isUploading, setIsUploading] = useState(false);
    const [uploadedFiles, setUploadedFiles] = useState([]);
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
                ]);
            });
    }, []);

    const onDrop = useCallback((acceptedFiles) => {
        if (acceptedFiles.length === 0) return;
        setUploadedFiles(prev => [...prev, ...acceptedFiles]);
    }, []);

    const handleRemoveFile = (index) => {
        setUploadedFiles(prev => prev.filter((_, i) => i !== index));
    };

    const handleStartAnalysis = async () => {
        if (uploadedFiles.length === 0) return;
        
        setIsUploading(true);
        setError(null);

        try {
            const formData = new FormData();
            formData.append('role', selectedRole);
            uploadedFiles.forEach(file => {
                formData.append('files', file);
            });

            const response = await fetch(`${API_URL}/api/analyze-batch`, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const err = await response.json();
                throw new Error(err.detail || 'Batch analysis failed');
            }

            const data = await response.json();
            setIsUploading(false);

            setTimeout(() => {
                onBatchUploadSuccess(data);
            }, 600);
        } catch (err) {
            setIsUploading(false);
            setError(err.message || 'Failed to connect to the backend. Is the server running?');
        }
    };

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            'application/pdf': ['.pdf'],
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
            'application/msword': ['.doc'],
        },
        multiple: true,
    });

    const renderContent = () => {
        if (isUploading) {
            return (
                <div className="upload-analyzing">
                    <div className="spinner" />
                    <div className="upload-analyzing-title">Analyzing {uploadedFiles.length} resumes...</div>
                    <div className="upload-analyzing-desc">
                        Rankings and insights will be ready shortly.
                    </div>
                </div>
            );
        }

        return (
            <>
                <div className="dropzone-icon">
                    <Users />
                </div>
                <div className="dropzone-text">Drag & drop multiple resumes here</div>
                <div className="dropzone-hint">Supports PDF, DOCX, and DOC (Upto 100+ files)</div>
                <button type="button" className="dropzone-btn">Browse Files</button>
            </>
        );
    };

    return (
        <div className="upload-view">
            <div className="upload-header">
                <h1 className="upload-title">Batch Candidate Ranking</h1>
                <p className="upload-subtitle">
                    Upload multiple resumes to find the best match for the target role.
                </p>
            </div>

            <div className="role-selector">
                <label className="role-label">Target Role</label>
                <RoleSearchDropdown
                    roles={roles}
                    selectedRole={selectedRole}
                    onSelect={setSelectedRole}
                />
            </div>

            {!isUploading && uploadedFiles.length > 0 && (
                <div className="batch-files-list">
                    <h3>Selected Files ({uploadedFiles.length})</h3>
                    <div className="files-container">
                        {uploadedFiles.map((f, i) => (
                            <div key={i} className="file-item">
                                <span className="file-name">{f.name}</span>
                                <button className="remove-file-btn" onClick={() => handleRemoveFile(i)}><X size={16}/></button>
                            </div>
                        ))}
                    </div>
                    <button className="btn-primary start-batch-btn" onClick={handleStartAnalysis}>
                        Start Batch Analysis
                    </button>
                </div>
            )}

            <div
                {...getRootProps()}
                className={`dropzone ${isDragActive ? 'drag-active' : ''}`}
                style={{ marginTop: uploadedFiles.length > 0 ? '2rem' : '0' }}
            >
                <input {...getInputProps()} />
                {renderContent()}
            </div>

            {error && (
                <div className="upload-error" style={{ marginTop: '1rem' }}>
                    <span>⚠ {error}</span>
                </div>
            )}
            
            <style>{`
            .batch-files-list {
                width: 100%;
                max-width: 520px;
                background: var(--bg-card);
                border: 1px solid var(--border-color);
                border-radius: var(--radius-md);
                padding: 1.5rem;
                margin-bottom: 1rem;
            }
            .batch-files-list h3 {
                margin-bottom: 1rem;
                font-size: 1rem;
                color: var(--text-primary);
            }
            .files-container {
                max-height: 200px;
                overflow-y: auto;
                margin-bottom: 1rem;
                display: flex;
                flex-direction: column;
                gap: 0.5rem;
            }
            .file-item {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0.5rem 0.75rem;
                background: var(--bg-tertiary);
                border-radius: var(--radius-sm);
                font-size: 0.85rem;
                color: var(--text-secondary);
            }
            .file-name {
                white-space: nowrap;
                overflow: hidden;
                text-overflow: ellipsis;
                max-width: 90%;
            }
            .remove-file-btn {
                color: var(--danger);
                cursor: pointer;
            }
            .remove-file-btn:hover {
                color: #ff8a8a;
            }
            .start-batch-btn {
                width: 100%;
                justify-content: center;
            }
            `}</style>
        </div>
    );
};

export default BatchUpload;
