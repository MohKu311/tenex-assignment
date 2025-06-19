"use client";

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';
import FileUpload from '../../components/FileUpload';

export default function DashboardPage() {
  const router = useRouter();

  useEffect(() => {
    const loggedIn = localStorage.getItem('loggedIn');
    if (loggedIn !== 'true') {
      router.push('/login');
    }
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('loggedIn');
    router.push('/login');
  };

  return (
    <main className="min-h-screen p-8 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">SOC Log Uploader</h1>
        <button
          onClick={handleLogout}
          className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition"
        >
          Logout
        </button>
      </div>

      <FileUpload />
    </main>
  );
}
