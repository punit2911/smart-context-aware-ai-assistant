// Import the new performance tracking functions
import { onCLS, onFID, onFCP, onLCP, onTTFB } from 'web-vitals';

const reportWebVitals = (onPerfEntry) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    // Use the new functions for performance tracking
    onCLS(onPerfEntry);  // Cumulative Layout Shift
    onFID(onPerfEntry);  // First Input Delay
    onFCP(onPerfEntry);  // First Contentful Paint
    onLCP(onPerfEntry);  // Largest Contentful Paint
    onTTFB(onPerfEntry); // Time to First Byte
  }
};

export default reportWebVitals;

