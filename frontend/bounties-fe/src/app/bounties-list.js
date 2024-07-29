'use client';

import styles from "./page.module.css";
import { useEffect, useState } from "react";


export default function BountiesList() {

    const [bounties, setBounties] = useState([]);

    function getBounties() {
      fetch("http://localhost:8000/api/bounties")
        .then(response => response.json())
        .then(data => setBounties(data))
        .catch(error => console.log(error));
    }

    useEffect(() => {
      getBounties();
    }, []);

    return (
    <>
    <div id={styles.bounties}>
    {bounties.map((bounty) => {
      return (
        <div className={styles.bounty} key={bounty.id}>
          <span className={styles.bountyTitle}>
            <a>{bounty.title}</a>
          </span>
          <span className={styles.bountyAmount}>${bounty.reward}</span>
      </div>
      );
    })}
    </div>
    </>
    );
}