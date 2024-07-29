import Link from "next/link";
import styles from "./page.module.css";

export default function Header() {
  return (
    <div id={styles.header}>
      <Link href="/">
        <h1 id={styles.title}>Software bounties</h1>
      </Link>
      <button id={styles.loginButton}>Login</button>
    </div>
  );
}