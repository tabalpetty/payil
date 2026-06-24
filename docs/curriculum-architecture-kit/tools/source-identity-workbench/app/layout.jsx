import "./globals.css";

export const metadata = {
  title: "Source Identity Workbench",
  description: "Layer -2 source identity checkpoint before extraction and decomposition.",
  manifest: "/manifest.webmanifest"
};

export const viewport = {
  themeColor: "#253238"
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
