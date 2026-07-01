import Modal from "../Modal/Modal";
import Button from "../Button/Button";

function ConfirmDialog({
    open,
    title,
    message,
    onCancel,
    onConfirm,
}) {

    return (

        <Modal
            open={open}
            onClose={onCancel}
        >

            <h2
                style={{
                    marginBottom: 12,
                }}
            >
                {title}
            </h2>

            <p
                style={{
                    marginBottom: 24,
                    color: "var(--slate)",
                }}
            >
                {message}
            </p>

            <div
                style={{
                    display: "flex",
                    gap: 12,
                    justifyContent: "flex-end",
                }}
            >

                <Button
                    variant="secondary"
                    onClick={onCancel}
                >
                    Cancelar
                </Button>

                <Button
                    onClick={onConfirm}
                >
                    Eliminar
                </Button>

            </div>

        </Modal>

    );

}

export default ConfirmDialog;