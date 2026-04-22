export const metadata = {
  title: "URL Shortener",
  description: "Simple URL shortener frontend",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
