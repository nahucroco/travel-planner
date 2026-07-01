import "./Button.css";

function Button({
    children,
    onClick,
    variant = "primary",
    full = false,
    size,
    ...props
}) {
    const classes = [
        "button",
        `button-${variant}`,
        full ? "button-full" : "",
        size === "sm" ? "button-sm" : "",
    ].filter(Boolean).join(" ");

    return (
        <button className={classes} onClick={onClick} {...props}>
            {children}
        </button>
    );
}

export default Button;
