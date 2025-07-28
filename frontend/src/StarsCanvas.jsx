import React from "react";
import { useStars } from "./useStars";

export default function StarsCanvas() {
  useStars();
  return <canvas className="stars"></canvas>;
}
