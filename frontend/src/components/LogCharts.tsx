"use client";

import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, Legend } from "recharts";

type LogEntry = {
  action: string;
  threat_type: string;
};

type Props = {
  logs: LogEntry[];
};

export default function LogCharts({ logs }: Props) {
  const actionData = logs.reduce<Record<string, number>>((acc, log) => {
    acc[log.action] = (acc[log.action] || 0) + 1;
    return acc;
  }, {});

  const threatData = logs.reduce<Record<string, number>>((acc, log) => {
    const type = log.threat_type || "none";
    acc[type] = (acc[type] || 0) + 1;
    return acc;
  }, {});

  const barData = Object.entries(actionData).map(([key, value]) => ({
    action: key,
    count: value,
  }));

  const pieData = Object.entries(threatData).map(([key, value]) => ({
    name: key,
    value,
  }));

  const COLORS = ["#0088FE", "#FF8042", "#00C49F", "#FFBB28", "#8884d8", "#d62728"];

  return (
    <div className="space-y-8 mt-8">
      <h3 className="text-lg font-semibold">Log Summary Charts</h3>

      <div className="w-full flex flex-col md:flex-row gap-8">
        {/* Bar Chart */}
        <div className="w-full h-64 bg-white rounded shadow p-4">
          <h4 className="font-bold mb-2">Actions Count</h4>
          <ResponsiveContainer width="100%" height="90%">
            <BarChart data={barData}>
              <XAxis dataKey="action" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="#8884d8" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Pie Chart */}
        <div className="w-full h-64 bg-white rounded shadow p-4">
          <h4 className="font-bold mb-2">Threat Type Breakdown</h4>
          <ResponsiveContainer width="100%" height="90%">
            <PieChart>
              <Pie
                data={pieData}
                dataKey="value"
                nameKey="name"
                outerRadius={70}
                label
              >
                {pieData.map((_, index) => (
                  <Cell key={index} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
