import { NextResponse } from "next/server";
import { discoverSourceCandidates } from "../../lib/verification";

export async function POST(request) {
  const input = await request.json();
  return NextResponse.json(discoverSourceCandidates(input));
}
