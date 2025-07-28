// Star & glitter animation for React
import { useEffect } from 'react';

export function useStars() {
  useEffect(() => {
    const canvas = document.querySelector('.stars');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let w = window.innerWidth;
    let h = window.innerHeight;
    canvas.width = w;
    canvas.height = h;
    let stars = [];
    function randomStar() {
      return {
        x: Math.random() * w,
        y: Math.random() * h,
        r: Math.random() * 1.2 + 0.5,
        o: Math.random() * 0.5 + 0.5,
        s: Math.random() * 0.5 + 0.2
      };
    }
    for (let i = 0; i < 120; i++) stars.push(randomStar());
    function drawStars() {
      ctx.clearRect(0, 0, w, h);
      for (let s of stars) {
        ctx.save();
        ctx.globalAlpha = s.o;
        ctx.beginPath();
        ctx.arc(s.x, s.y, s.r, 0, 2 * Math.PI);
        ctx.fillStyle = '#fff';
        ctx.shadowColor = '#e0b3ff';
        ctx.shadowBlur = 12;
        ctx.fill();
        ctx.restore();
        // Twinkle
        s.o += (Math.random() - 0.5) * 0.04;
        if (s.o < 0.3) s.o = 0.3;
        if (s.o > 1) s.o = 1;
      }
    }
    const interval = setInterval(drawStars, 60);
    function handleResize() {
      w = window.innerWidth;
      h = window.innerHeight;
      canvas.width = w;
      canvas.height = h;
      stars = [];
      for (let i = 0; i < 120; i++) stars.push(randomStar());
    }
    window.addEventListener('resize', handleResize);
    return () => {
      clearInterval(interval);
      window.removeEventListener('resize', handleResize);
    };
  }, []);
}
