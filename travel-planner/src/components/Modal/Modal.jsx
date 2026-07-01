import "./Modal.css";

function Modal({ open, onClose, children }) {
    if (!open) return null;

    return (
        <div className="modal-overlay" onClick={onClose}>
            <div className="modal" onClick={e => e.stopPropagation()}>
                <div className="modal-drag" />
                {onClose && (
                    <button className="modal-close" onClick={onClose}>✕</button>
                )}
                {children}
            </div>
        </div>
    );
}

export default Modal;
