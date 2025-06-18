import FileUpload from '../components/FileUpload';

export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-white p-8">
      <h1 className="text-2xl font-bold mb-4">SOC Log Uploader</h1>
      <FileUpload />
    </main>
  );
}
