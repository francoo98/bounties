import styles from "./page.module.css";

export default function Header() {
    return (
      <div id={styles.header}>
      <h1 id={styles.title}>Software bounties</h1>
      <button id={styles.loginButton}>Login</button>
      </div>
    );
}