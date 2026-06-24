import { NextResponse } from "next/server";
import { verifyOfficialSource } from "../../lib/verification";

export async function POST(request) {
  const input = await request.json();
  const verification = await verifyOfficialSource(input);
  return NextResponse.json({ verification });
}

